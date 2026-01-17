# Modelo de clasificación de dialectos

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
import joblib

def train_dialect_classifier(features, labels):
    """Entrena un modelo de clasificación de dialectos con SVM."""
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
    model = SVC(kernel='linear')
    model.fit(X_train, y_train)
    joblib.dump(model, "models/dialect_classifier.pkl")
    print("[INFO] Modelo entrenado y guardado.")
    return model

def predict_dialect(model, features):
    """Predice el dialecto de un audio procesado."""
    return model.predict([features])
