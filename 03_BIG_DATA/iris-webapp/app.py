import joblib
from flask import Flask, request, jsonify, session, url_for, redirect, render_template
from flower_form import FlowerForm


# Cargamos los modelos guardados en saved_models
knn_path = "models/iris_knn.pkl"
enc_path = "models/iris_label_encoder.pkl"
knn_loaded = joblib.load(knn_path)
encoder_loaded = joblib.load(enc_path)

def make_prediction(model, encoder, sample_json):
    # parse input from request
    SepalLengthCm = sample_json['SepalLengthCm']
    SepalWidthCm = sample_json['SepalWidthCm']
    PetalLengthCm = sample_json['PetalLengthCm']
    PetalWidthCm = sample_json['PetalWidthCm']

    # Make an input vector
    flower = [[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]]

    # Predict
    prediction_raw = model.predict(flower)

    # Convert Species index to Species name
    prediction_real = encoder.inverse_transform(prediction_raw)

    return prediction_real[0]


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


@app.route("/", methods=['GET','POST'])
def index():
    form = FlowerForm()

    if form.validate_on_submit():
        session['SepalLengthCm'] = form.SepalLengthCm.data
        session['SepalWidthCm'] = form.SepalWidthCm.data
        session['PetalLengthCm'] = form.PetalLengthCm.data
        session['PetalWidthCm'] = form.PetalWidthCm.data

        return redirect(url_for("prediction"))
    return render_template("home.html", form=form)


@app.route('/prediction')
def prediction():
    content = {'SepalLengthCm': float(session['SepalLengthCm']), 'SepalWidthCm': float(session['SepalWidthCm']),
               'PetalLengthCm': float(session['PetalLengthCm']), 'PetalWidthCm': float(session['PetalWidthCm'])}

    results = make_prediction(knn_loaded, encoder_loaded, content)

    return render_template('prediction.html', results=results)


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080)
    app.run()