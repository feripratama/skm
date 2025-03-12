from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data unsur pelayanan
unsur_pelayanan = [
    "Persyaratan pelayanan",
    "Prosedur pelayanan",
    "Waktu pelayanan",
    "Biaya/tarif pelayanan",
    "Produk spesifikasi jenis pelayanan",
    "Kompetensi pelaksana",
    "Perilaku pelaksana",
    "Maklumat pelayanan",
    "Penanganan pengaduan, saran dan masukan"
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Mengambil nilai dari formulir
        nilai_persepsi = [float(request.form[f"nilai_{i}"]) for i in range(len(unsur_pelayanan))]
        
        # Menghitung nilai rata-rata tertimbang per unsur
        bobot = 0.11
        nilai_rata_rata_tertimbang = [nilai * bobot for nilai in nilai_persepsi]
        
        # Menghitung SKM unit pelayanan
        skm_unit_pelayanan = sum(nilai_rata_rata_tertimbang) * 25
        
        # Menentukan mutu pelayanan berdasarkan interval
        if 25 <= skm_unit_pelayanan <= 43.75:
            mutu = "Tidak Baik (D)"
        elif 43.76 <= skm_unit_pelayanan <= 62.50:
            mutu = "Kurang Baik (C)"
        elif 62.51 <= skm_unit_pelayanan <= 81.25:
            mutu = "Baik (B)"
        else:
            mutu = "Sangat Baik (A)"
        
        # Redirect ke halaman hasil
        return render_template("result.html", skm=skm_unit_pelayanan, mutu=mutu)
    
    return render_template("index.html", unsur_pelayanan=unsur_pelayanan)

@app.route("/result")
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)