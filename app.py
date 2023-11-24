from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Muat model
model = joblib.load('model_classification.joblib')

# Fungsi untuk menghitung kategori udara berdasarkan model
def hitung_kategori_udara(PM10, CO, O3, SO2):
    # ... Logika lainnya ...

    # Contoh penggunaan model (harap disesuaikan dengan format input model Anda)
    input_model = [[PM10, CO, O3, SO2]]
    prediksi_kategori_udara = model.predict(input_model)[0]

    return prediksi_kategori_udara

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        PM10 = int(request.form['PM10'])
        CO = int(request.form['CO'])
        O3 = int(request.form['O3'])
        SO2 = int(request.form['S02'])

        kategori = hitung_kategori_udara(PM10, CO, O3, SO2)

        return render_template('index.html', kategori=kategori)
    else:
        return render_template('index.html', kategori="")

if __name__ == '__main__':
    app.run(debug=True)
