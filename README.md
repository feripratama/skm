# Panduan Menjalankan Aplikasi

## Prasyarat
- Python 3.6 atau lebih tinggi
- pip (Python package manager)

## Langkah-langkah Instalasi

1. **Clone repository ini**
    ```bash
    git clone https://github.com/username/survey.git
    cd survey
    ```

2. **Buat virtual environment (opsional tapi disarankan)**
    ```bash
    python -m venv venv
    ```

3. **Aktifkan virtual environment**
    - Windows:
      ```bash
      venv\Scripts\activate
      ```
    - macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install dependensi**
    ```bash
    pip install -r requirements.txt
    ```

## Menjalankan Aplikasi

1. **Jalankan aplikasi**
    ```bash
    python app.py
    ```

2. **Buka aplikasi di browser**
    Buka [http://localhost:5000](http://localhost:5000) di browser Anda

## Menghentikan Aplikasi

1. **Tekan `Ctrl+C` di terminal untuk menghentikan server**

2. **Nonaktifkan virtual environment**
    ```bash
    deactivate
    ```