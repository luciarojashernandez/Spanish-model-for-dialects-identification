# Spanish Dialect Classifier (Pilot)

Este proyecto implementa un sistema de clasificación automática para distinguir entre dos variantes del español —La Habana y Ciudad de México— a partir de muestras orales etiquetadas.

## 📁 Estructura del proyecto

```
SPANISH-MODEL-FOR-DIALECTS/
├── data/                         # Corpus organizado por ciudad y tipo de enunciado
├── models/                       # Modelo entrenado (.pkl)
├── scripts/                      # Scripts principales
│   ├── train_real_classifier.py
│   ├── batch_predict.py
│   └── visualize_predictions.py
└── src/                          # Funciones auxiliares
    ├── data_preprocessing.py
    ├── feature_extraction.py
    └── dialect_classifier.py
```

## ⚙️ Requisitos

- Python 3.10+
- `librosa`
- `scikit-learn`
- `numpy`
- `pandas`
- `matplotlib` (si se visualiza)

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

## 🚀 Cómo usar

### 1. Entrenar el modelo

```bash
python -m scripts.train_real_classifier
```

### 2. Predecir dialectos en los audios

```bash
python -m scripts.batch_predict
```

### 3. Visualizar resultados

```bash
python -m scripts.visualize_predictions
```

## 📦 Salida esperada

Un archivo `predicciones_dialectos.csv` con los resultados, y estadísticas impresas en consola.

## 🔐 Repositorio privado

Este repositorio es parte de una tesina de licenciatura y se mantiene privado. Disponible bajo solicitud con fines académicos.
