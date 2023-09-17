import joblib


# Cargamos los modelos guardados en saved_models
knn_path = "../models/iris_knn.pkl"
enc_path = "../models/iris_label_encoder.pkl"
knn_loaded = joblib.load(knn_path)
encoder_loaded = joblib.load(enc_path)


