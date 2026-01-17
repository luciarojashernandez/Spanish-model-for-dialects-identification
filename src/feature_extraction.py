# Extracción de características (MFCCs, espectrogramas)
#Este módulo extrae MFCCs y contraste espectral, características clave para la clasificación de dialectos.

import librosa
import numpy as np

def extract_mfcc(audio, sr, n_mfcc=13):
    """Extrae coeficientes MFCC del audio."""
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc)
    print(f"[INFO] MFCCs extraídos con forma: {mfccs.shape}")
    return mfccs

def extract_spectral_contrast(audio, sr):
    """Extrae el contraste espectral."""
    contrast = librosa.feature.spectral_contrast(y=audio, sr=sr)
    print(f"[INFO] Contraste espectral extraído con forma: {contrast.shape}")
    return contrast
