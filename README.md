# 💫Klasifikasi Rumah Adat Indonesia dengan CNN dan MobileNet💫

## 🧷Deskripsi Projeck

Projeck ini bertujuan untuk mengembangkan sebuah sistem klasifikasi gambar yang dapat mengenali dan membedakan gambar-gambar yang termasuk dalam kategori *"Gadang"* dari Sumatera Barat, *"Honai"* dari Papua, *"Jonglo"* dari Jawa, *"Panjang"* dari Kalimantan, dan *"Tongkonan"* dari Sulawesi Selatan. Proyek ini tidak hanya bertujuan untuk mengidentifikasi jenis rumah adat berdasarkan ciri visualnya tetapi juga diharapkan dapat membantu melestarikan budaya dan warisan arsitektur tradisional Indonesia melalui teknologi modern. Dengan memanfaatkan dataset gambar yang relevan dan teknik pembelajaran mesin, sistem ini akan dilatih untuk mengenali pola dan karakteristik visual unik dari setiap kategori rumah adat. 

Projeck ini menggunakan Dataset yang diambil dari [Kaggle](https://www.kaggle.com/datasets/rariffirmansah/rumah-adat), yang telah dilakukan Preprocessing seperti antara lain Resizing, Normalization dan  Augmentation, yang disimpan pada link [ini](https://drive.google.com/drive/folders/1PUx-3EpQFIIxOXHD52Pk1Y1s8KCF5SVZ?usp=drive_link). Adapun Model yang telah dilatih dapat diaskses [disini](https://drive.google.com/drive/folders/15b_OdgaOHIArKq-llL0N_4vj2k9QGTFG?usp=sharing).

---

## 🛠️Langkah Instalasi
1. **Clone Repository:**
   ```bash
   git init
   git add .
   git commit -m "Inisialisasi proyek"
   git remote add origin https://github.com/AlfaGhiffari/UAP_Machine-Learning.git
   git branch -M main
   git push -u origin main

   commit
   git status
   git add (sesuai file yang ditambahkan)
   git commit -m "coba"
   git push origin main
  
   ```

2. **Buat Virtual Environment:**
   ```bash
   python -m venv env
   env\Scripts\activate   # Untuk Windows
   ```

3. **Instal Dependencies:**
   ```bash
   pip install pdm
   pdm init
   pdm add streamlit
   pdm add tensorflow
   pdm add joblib
   pdm add scikit-learn
   pip install -r requirements.txt
   ```

4. **Jalankan Aplikasi Web:**
   ```bash
   pdm run start
   ```
---

## 🖋️Deskripsi Model
### CNN Model
#### Preprocessing
Preprocessing yang dilakukan antara lain adalah resizing (128,128), lalu rescale / normalization dengan rentang 1./255, dilanjut dengan melakukan splitting dataset menjadi 3 (Training, Validation, dan Testing)

#### Modelling & Evaluation
Berikut adalah hasil dari fitting CNN Model yang telah dibangun :

![image](https://github.com/user-attachments/assets/190b53e9-950c-465d-bbd3-f23f4a1931b3)

Plot diatas menunjukkan bahwa Training accuracy meningkat secara bertahap hingga mencapai sekitar 96%, Testing accuracy juga meningkat secara bertahap hingga mencapai sekitar 94%

![image](https://github.com/user-attachments/assets/ff4b4f8d-5e7a-4a28-8397-1000cb35cdc0)

Dapat dilihat pada plot loss di atas, training loss lebih tinggi dibandingkan validation loss. Hal ini bisa disebabkan oleh model yang underfitting, regularisasi yang berlebihan, atau distribusi data yang tidak konsisten.

![image](https://github.com/user-attachments/assets/46b5cda0-435a-42d2-b3d4-e5709b827676)

Gambar di atas merupakan Classification Report dari model setelah dilakukan prediksi terhadap testing set. Dapat dilihat bahwa akurasinya mencapai 95%. Pada label 'Gadang', model berhasil mencapai precision, recall, dan f1-score 100%. Meskipun label 'Honai' memiliki recall yang sempurna (100%), precision-nya sedikit lebih rendah (86%), yang menunjukkan beberapa kesalahan pada prediksi kelas tersebut. Secara keseluruhan, model menunjukkan performa yang sangat baik dengan f1-score rata-rata 0.95, baik untuk label individual maupun secara keseluruhan.

### MobileNet
#### Preprocessing
Preprocessing yang dilakukan antara lain adalah resizing (299,299) sesuai rekomendasi Inception-V3, lalu rescale / normalization dengan rentang 1./255, lalu melakukan augmentasi dengan parameter seperti sheer_range yang diatur ke 0.2, zoom_range diatur ke 0.2, dan horizontal_flip. Setelah augmentasi selesai dilakukan, langkah terakhir adalah splitting dataset menjadi 3 (Training, Validation, dan Testing) sesuai dengan penjelasan pada Dataset.

#### Modelling & Evaluation
Berikut adalah hasil dari fitting MobileNet Model yang telah dibangun :

![image](https://github.com/user-attachments/assets/fbf2dd15-c02f-4557-b8f5-9342cb64bc8a)

Plot di atas menunjukkan bahwa baik training accuracy maupun validation accuracy keduanya mendekati 100%. Hal ini mengindikasikan bahwa model memiliki performa yang sangat baik pada kedua data tersebut dan tidak mengalami overfitting. Model tampaknya dapat belajar dengan baik dari data training dan juga generalisasi dengan baik pada data validasi. Namun, untuk memastikan model tidak hanya menghafal data, disarankan untuk melakukan evaluasi lebih lanjut dengan dataset yang lebih besar atau data yang belum terlihat (testing set).

![image](https://github.com/user-attachments/assets/ba5e99d8-a3e6-491a-9e49-48d6cdece493)

Dapat dilihat pada plot loss diatas. Training dan Val Loss sama - sama turun, namun val_loss cenderung lebih tinggi dibanding training_loss nya. Hal ini mungkin saja disebabkan karena terjadi Overfitting pada Model

![image](https://github.com/user-attachments/assets/220aa91a-018e-46ba-95e3-d9900b55369b)

Gambar di atas merupakan Classification Report dari model setelah dilakukan prediksi terhadap testing set. Dapat dilihat bahwa akurasinya mencapai 100%, dengan precision, recall, dan f1-score hampir sempurna untuk setiap label. Model berhasil mencapai hasil 100% pada label 'Honai', 'Panjang', dan 'Tongkonan', serta sangat mendekati 100% pada label lainnya seperti 'Gadang' dan 'Joglo'. Secara keseluruhan, model menunjukkan performa yang sangat baik dengan nilai f1-score rata-rata 1.00, yang menunjukkan bahwa model dapat menggeneralisasi dengan sangat baik pada data validasi dan tidak mengalami overfitting.






