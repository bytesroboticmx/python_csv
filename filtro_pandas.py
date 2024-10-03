import pandas as pd

df = pd.read_csv('movies.csv')

filtro =df[df['Año']>=1990]
print(filtro)
