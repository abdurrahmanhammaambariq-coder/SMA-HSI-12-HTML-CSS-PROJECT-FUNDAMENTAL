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
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'ini-rahasia-banget-loh'

semua_pesan = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/bukutamu', methods=['GET', 'POST'])
def bukutamu():
    global semua_pesan
 
    if request.method == 'POST':
        nama = request.form.get("nama","").strip()
        pesan = request.form.get("pesan","").strip()
    
        if nama == 'fulan':
            flash('Anda tidak diperbolehkan mengirim pesan!', 'failed')
            return redirect(url_for('buku_tamu'))

        semua_pesan.append({'nama': nama, 'pesan': pesan})

        flash('Pesan Anda telah berhasil dikirim!', 'success')

        return redirect(url_for('buku_tamu'))
    return render_template("bukutamu.html",semua_pesan=semua_pesan)

if __name__ == "__main__":
    app.run(debug=True)



