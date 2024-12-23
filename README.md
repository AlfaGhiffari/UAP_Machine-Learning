# 💫Klasifikasi Rumah Adat Indonesia dengan CNN dan MobileNet💫

## 🧷Deskripsi Projeck

Projeck ini bertujuan untuk mengembangkan sebuah sistem klasifikasi gambar yang dapat mengenali dan membedakan gambar-gambar yang termasuk dalam kategori *"Gadang"* dari Sumatera Barat, *"Honai"* dari Papua, *"Jonglo"* dari Jawa, *"Panjang"* dari Kalimantan, dan *"Tongkonan"* dari Sulawesi Selatan. Proyek ini tidak hanya bertujuan untuk mengidentifikasi jenis rumah adat berdasarkan ciri visualnya tetapi juga diharapkan dapat membantu melestarikan budaya dan warisan arsitektur tradisional Indonesia melalui teknologi modern. Dengan memanfaatkan dataset gambar yang relevan dan teknik pembelajaran mesin, sistem ini akan dilatih untuk mengenali pola dan karakteristik visual unik dari setiap kategori rumah adat. 

Projeck ini menggunakan Dataset yang diambil dari [Kaggle](https://www.kaggle.com/datasets/rariffirmansah/rumah-adat), yang telah dilakukan Preprocessing seperti antara lain Resizing, Normalization dan  Augmentation, yang disimpan pada link [ini](https://drive.google.com/drive/folders/1PUx-3EpQFIIxOXHD52Pk1Y1s8KCF5SVZ?usp=drive_link).

## 🛠️Langkah Instalasi
1. **Clone Repository:**
   ```bash
   git init
   git add .
   git commit -m "Inisialisasi proyek"
   git remote add origin https://github.com/marwasaniyya/UAP.git
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
   
## 🛠️Langkah Instalasi



