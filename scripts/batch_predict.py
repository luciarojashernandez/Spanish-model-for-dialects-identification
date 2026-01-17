import os
import numpy as np
import pandas as pd
from src.data_preprocessing import load_audio
from src.feature_extraction import extract_mfcc
from src.dialect_classifier import predict_dialect
import joblib

# Cargar el modelo
model = joblib.load("models/dialect_classifier.pkl")

# Definir las carpetas a procesar
base_dirs = [
    "data/ciudad_de_mexico/enunciativas",
    "data/ciudad_de_mexico/declarativas",
    "data/la_habana/enunciativas",
    "data/la_habana/declarativas"
]

results = []

# Recorrer todas las carpetas y procesar los audios .wav
for folder in base_dirs:
    for file in os.listdir(folder):
        if file.endswith(".wav"):
            file_path = os.path.join(folder, file)
            audio, sr = load_audio(file_path)
            if audio is None:
                continue
            mfcc = extract_mfcc(audio, sr)
            mfcc_mean = np.mean(mfcc, axis=1)
            predicted = predict_dialect(model, mfcc_mean)
            results.append({
                "archivo": file,
                "carpeta_origen": folder,
                "ciudad_detectada": predicted[0],
                "duracion_s": round(len(audio) / sr, 2)
            })

# Guardar resultados
df = pd.DataFrame(results)
df.to_csv("predicciones_dialectos.csv", index=False)
print("[INFO] Predicciones guardadas en predicciones_dialectos.csv")
