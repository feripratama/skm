from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data pendidikan
daftar_pendidikan = ["SD", "SMP", "SMA", "D1/D2/D3", "D4/S1", "S2", "S3"]

# Data pekerjaan
daftar_pekerjaan = [
    "Wiraswasta",
    "Karyawan Swasta",
    "ASN",
    "TNI/POLRI",
    "Buruh/Petani",
    "Pekerja Lepas (Freelancer)",
    "Lainnya"
]

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
        # Mengambil data profil
        gender = request.form.get('gender')
        pendidikan = request.form.get('pendidikan')
        pekerjaan = request.form.get('pekerjaan')
        if pekerjaan == 'Lainnya':
            pekerjaan = request.form.get('pekerjaan_lainnya')

        # Mengambil nilai persepsi
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
        
        # Redirect ke halaman hasil dengan parameter
        return redirect(url_for('result', 
                              skm=skm_unit_pelayanan, 
                              mutu=mutu,
                              gender=gender,
                              pendidikan=pendidikan,
                              pekerjaan=pekerjaan))
    
    return render_template("index.html", 
                         unsur_pelayanan=unsur_pelayanan,
                         daftar_pendidikan=daftar_pendidikan,
                         daftar_pekerjaan=daftar_pekerjaan)

@app.route("/result")
def result():
    if not all(key in request.args for key in ['skm', 'mutu', 'gender', 'pendidikan', 'pekerjaan']):
        return redirect(url_for('index'))
    return render_template("result.html",
                         skm=float(request.args.get('skm')),
                         mutu=request.args.get('mutu'),
                         gender=request.args.get('gender'),
                         pendidikan=request.args.get('pendidikan'),
                         pekerjaan=request.args.get('pekerjaan'))

if __name__ == "__main__":
    app.run(debug=True)
