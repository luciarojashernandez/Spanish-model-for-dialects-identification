# Procesamiento de audimport librosa
#Objetivo: Verificar que el audio se carga correctamente y se normaliza.
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

def load_audio(file_path, sr=22050):
    """Carga un archivo de audio y lo normaliza a una frecuencia de muestreo estándar."""
    try:
        signal, sample_rate = librosa.load(file_path, sr=sr)
        print(f"[INFO] Audio cargado correctamente: {file_path}")
        print(f"    - Duración: {len(signal)/sample_rate:.2f} segundos")
        print(f"    - Frecuencia de muestreo: {sample_rate} Hz")
        return signal, sample_rate
    except Exception as e:
        print(f"[ERROR] No se pudo cargar el audio: {e}")
        return None, None

def plot_waveform(audio, sr):
    """Grafica la forma de onda del audio."""
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(audio, sr=sr)
    plt.title("Forma de Onda del Audio")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.show()