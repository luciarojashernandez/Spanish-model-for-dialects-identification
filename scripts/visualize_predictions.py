import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("predicciones_dialectos.csv")

# Mostrar todas las predicciones
print("\n📄 Predicciones individuales:")
print(df)

# Contar cuántos audios fueron clasificados como cada dialecto
conteo = df["ciudad_detectada"].value_counts()
print("\n📊 Conteo de predicciones por dialecto:")
print(conteo)

# Gráfico de barras
plt.figure(figsize=(6, 4))
conteo.plot(kind='bar', color='skyblue')
plt.title("Cantidad de audios por dialecto detectado")
plt.xlabel("Dialecto")
plt.ylabel("Cantidad de audios")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
