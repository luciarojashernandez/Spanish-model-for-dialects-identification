# # scripts/train_model.py
# import os
# import numpy as np
# from src.data_preprocessing import load_audio
# from src.feature_extraction import extract_mfcc, extract_spectral_contrast
# from src.dialect_classifier import train_dialect_classifier

# # Configura tus carpetas
# base_dir = "data"
# dialects = ["ciudad_de_mexico", "la_habana"]
# types = ["declarativas", "enunciativas"]

# features = []
# labels = []

# for dialect in dialects:
#     for typ in types:
#         folder_path = os.path.join(base_dir, dialect, typ)
#         for file_name in os.listdir(folder_path):
#             if file_name.endswith(".wav"):
#                 file_path = os.path.join(folder_path, file_name)
#                 audio, sr = load_audio(file_path)
#                 if audio is None:
#                     continue
                
#                 # Extraer características
#                 mfcc = extract_mfcc(audio, sr)
#                 contrast = extract_spectral_contrast(audio, sr)
                
#                 # Promediar las características para convertirlas a vector plano
#                 mfcc_mean = np.mean(mfcc, axis=1)
#                 contrast_mean = np.mean(contrast, axis=1)
#                 combined = np.concatenate((mfcc_mean, contrast_mean))
                
#                 features.append(combined)
#                 labels.append(dialect)

# # Convertir a arrays de NumPy
# features = np.array(features)
# labels = np.array(labels)

# # Entrenar modelo
# train_dialect_classifier(features, labels)
