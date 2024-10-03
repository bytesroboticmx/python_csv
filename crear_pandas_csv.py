import pandas as pd

# Leer un archivo CSV
df = pd.read_csv('movies.csv')

# Filtrar filas donde la edad sea mayor a 30
filtro = df[df['Año'] >= 2019]
print(filtro)
