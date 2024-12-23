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

## 🛠🖋️Deskripsi Model
### CNN Model
#### Preprocessing
Preprocessing yang dilakukan antara lain adalah resizing (128,128), lalu rescale / normalization dengan rentang 1./255, dilanjut dengan melakukan splitting dataset menjadi 3 (Training, Validation, dan Testing)

#### Modelling & Evaluation
Berikut adalah hasil dari fitting CNN Model yang telah dibangun :
![image](https://github.com/user-attachments/assets/190b53e9-950c-465d-bbd3-f23f4a1931b3)
Plot diatas menunjukkan bahwa Training accuracy meningkat secara bertahap hingga mencapai sekitar 96%, Testing accuracy juga meningkat secara bertahap hingga mencapai sekitar 94%

![image](https://github.com/user-attachments/assets/ff4b4f8d-5e7a-4a28-8397-1000cb35cdc0)
Dapat dilihat pada plot loss di atas, training loss lebih tinggi dibandingkan validation loss. Hal ini bisa disebabkan oleh model yang underfitting, regularisasi yang berlebihan, atau distribusi data yang tidak konsisten.




