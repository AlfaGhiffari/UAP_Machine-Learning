import streamlit as st
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
import os
import gdown
from PIL import Image
import time

# Set page configuration first
st.set_page_config(
    page_title="Traditional House Classifier",
    page_icon="🏠",
    layout="wide"
)

# Path untuk model
CNN_model_path = 'Model\CNN.keras'
MobileNet_model_path = 'Model\MobileNet.keras'

# URL untuk mengunduh model jika tidak ada di sistem
CNN_model_url = "https://drive.google.com/file/d/1z4BakZkT99_KhtRBClmczr_1cYaI71QP/view?usp=drive_link"
MobileNet_model_url = "https://drive.google.com/file/d/1VQt6DNr5Btqnli1SGIyBNDC_JpiE2lYQ/view?usp=drive_link"

# Fungsi untuk mengunduh model
@st.cache_resource
def download_model(model_path, model_url):
    os.makedirs("model", exist_ok=True)

    # Jika model belum ada, unduh dari Google Drive
    if not os.path.isfile(model_path):
        gdown.download(model_url, fuzzy=True, output=model_path)

# Fungsi untuk memuat model
@st.cache_resource
def load_model_from_path(model_path):
    return load_model(model_path)

# Mengunduh model jika belum ada
download_model(CNN_model_path, CNN_model_url)
download_model(MobileNet_model_path, MobileNet_model_url)

# Memuat model setelah diunduh
CNN_model = load_model_from_path(CNN_model_path)
MobileNet_model = load_model_from_path(MobileNet_model_path)

# Define class labels
labels = ['Gadang', 'Honai', 'Joglo', 'Panjang', 'Tongkonan']

# Function to predict the class of an uploaded image
def predict_image(model, img_path):
    # Load and preprocess the image
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    # Predict the class
    start_time = time.time()
    predictions = model.predict(img_array)
    elapsed_time = time.time() - start_time

    predicted_class_index = np.argmax(predictions)
    predicted_class = labels[predicted_class_index]
    confidence = predictions[0][predicted_class_index] * 100  

    return predicted_class, confidence, predictions[0], round(elapsed_time, 3)

# Streamlit UI
# Custom CSS for modern styling
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            color: #34495E;
            background-color: #F8F9FA;
        }
        .header-title {
            text-align: center;
            color: #2C3E50;
            font-size: 36px;
            margin-top: -20px;
        }
        .description {
            text-align: center;
            color: #7F8C8D;
            font-size: 16px;
            margin-bottom: 20px;
        }
        .prediction-card {
            background-color: #FFFFFF;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin: 20px;
        }
        .prediction-text {
            color: #27AE60;
            font-size: 24px;
            text-align: center;
            font-weight: bold;
        }
        .confidence-text {
            color: #8E44AD;
            font-size: 18px;
            text-align: center;
        }
        .progress-bar {
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<div class='header-title'>🏠 Classification of Traditional House Images</div>", unsafe_allow_html=True)
st.markdown("<div class='description'>Upload an image of a traditional house to classify it using deep learning models.</div>", unsafe_allow_html=True)

# Sidebar for file upload and model selection
uploaded_file = st.sidebar.file_uploader("Upload Image File:", type=['jpg', 'jpeg', 'png'])
model_option = st.sidebar.selectbox("Select Model:", ('CNN', 'MobileNet'))

# Main layout
if uploaded_file is not None:
    # Create a two-column layout
    col1, col2 = st.columns(2)

    # Display uploaded image in the first column
    with col1:
        st.markdown("<h4 style='color: #34495E;'>Uploaded Image</h4>", unsafe_allow_html=True)
        st.image(Image.open(uploaded_file), caption='Uploaded Image', use_container_width=True)

    # Predict and display results in the second column
    with col2:
        if st.button("🔍 Predict"):
            with st.spinner("Analyzing the image..."):
                # Load selected model
                model = CNN_model if model_option == 'CNN' else MobileNet_model
                
                # Perform prediction
                prediction, confidence, probabilities, prediction_time = predict_image(model, uploaded_file)

                # Display prediction results in a card
                st.markdown("""
                    <div class='prediction-card'>
                        <div class='prediction-text'>Prediction: {}</div>
                        <div class='confidence-text'>Confidence: {:.2f}%</div>
                        <div class='confidence-text'>Prediction Time: {:.3f} seconds</div>
                    </div>
                """.format(prediction, confidence, prediction_time), unsafe_allow_html=True)

                # Display probabilities for all classes with a progress bar
                st.markdown("<h4 style='color: #2980B9;'>Class Probabilities:</h4>", unsafe_allow_html=True)
                for i, prob in enumerate(probabilities):
                    st.progress(int(prob * 100))
                    st.markdown(f"<div style='color: #34495E;'>{labels[i]}: {prob * 100:.2f}%</div>", unsafe_allow_html=True)
