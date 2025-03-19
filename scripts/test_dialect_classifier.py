import numpy as np
from src.dialect_classifier import train_dialect_classifier

features = np.random.rand(10, 13)  # 10 muestras de MFCCs de 13 coeficientes
labels = np.array(["mexico", "habana", "madrid"] * 3 + ["mexico"])

model = train_dialect_classifier(features, labels)
