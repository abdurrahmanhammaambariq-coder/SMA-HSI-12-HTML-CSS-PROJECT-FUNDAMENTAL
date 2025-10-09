# # 1. Impor "cetakan" Flask
# from flask import Flask 
# # 2. Buat "objek" aplikasi dari cetakan tersebut 
# app = Flask(__name__) 
# # 3. Buat "alamat" atau "rute" untuk halaman utama
# @app.route('/')
# def halaman_utama(): 
# # 4. Tentukan apa yang harus ditampilkan di alamat ini 
#     return "Halo dari Server Flask!" 
# # 5. (Opsional tapi bagus) Baris untuk menjalankan aplikasi
# if __name__ == '__main__': 
#     app.run(debug=True) 



# latihan pertama
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/profil")
def halaman_profil():
    nama_penguguna = "Baba"
    hobi_pengguna = "bola"
    sekolah_pengguna = "HSI"
    return render_template("profil.html", user_name=nama_penguguna,user_hobby=hobi_pengguna,user_school=sekolah_pengguna)

@app.route('/bukutamu',methods=['GET','POST'])
def halaman_teman():
    if request.method == 'GET':
        return render_template('bukutamu.html')
    if request.method == 'POST':
        nama = request.form.get('nama')
        pesan = request.form.get('pesan')

    return render_template('bukutamu.html', nama=nama, pesan=pesan)


if __name__ == "__main__":
    app.run(debug=True)

