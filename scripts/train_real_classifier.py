from src.data_preprocessing import load_audio
from src.feature_extraction import extract_mfcc
from src.dialect_classifier import train_dialect_classifier
import os
import numpy as np

# Recorrer tus audios y extraer MFCCs
X = []
y = []

carpetas = {
    "mexico": "data/ciudad_de_mexico",
    "habana": "data/la_habana"
}

for dialecto, ruta_base in carpetas.items():
    for tipo in ["enunciativas", "declarativas"]:
        ruta = os.path.join(ruta_base, tipo)
        if not os.path.exists(ruta):
            continue
        for archivo in os.listdir(ruta):
            if archivo.endswith(".wav"):
                path = os.path.join(ruta, archivo)
                audio, sr = load_audio(path)
                if audio is not None:
                    mfcc = extract_mfcc(audio, sr)
                    mfcc_mean = np.mean(mfcc, axis=1)
                    X.append(mfcc_mean)
                    y.append(dialecto)
                    print(f"[INFO] Agregado {archivo} como {dialecto}")

# Convertir a arrays
X = np.array(X)
y = np.array(y)

print(f"\n✅ Total audios procesados: {len(y)}")
print(f"🧾 Distribución por clase: {dict(zip(*np.unique(y, return_counts=True)))}")

# Entrenar modelo real
model = train_dialect_classifier(X, y)
