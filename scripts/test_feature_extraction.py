# import sys
# import os

# # Agregar la raíz del proyecto al sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from src.data_preprocessing import load_audio
# from src.feature_extraction import extract_mfcc, extract_spectral_contrast

# audio_path = "data/test_samples/test1.wav"
# audio, sr = load_audio(audio_path)

# if audio is not None:
#     mfccs = extract_mfcc(audio, sr)
#     contrast = extract_spectral_contrast(audio, sr)


# #python -m scripts.test_feature_extraction
