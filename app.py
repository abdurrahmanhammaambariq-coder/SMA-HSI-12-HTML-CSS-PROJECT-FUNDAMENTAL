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
semua_pesan = []  # database sementara

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/bukutamu', methods=['GET', 'POST'])
def halaman_teman():
    global semua_pesan
    
    if request.method == 'POST':
        nama = request.form.get('nama')
        pesan = request.form.get('pesan')

        data_baru = {'nama': nama, 'pesan': pesan}
        semua_pesan.append(data_baru)

    return render_template('bukutamu.html', semua_pesan=semua_pesan)

if __name__ == "__main__":
    app.run(debug=True)
