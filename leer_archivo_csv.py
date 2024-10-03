1#Programa en python que lee un archivo externo con extension .csv e imprime en pantalla su contenido.
#Autor: Dr. Aldo Glez V.
#Version: 0.1
#Fecha: 18/09/2024
#Importamos libreria estandar csv
import csv
#Lee el archivo .csv en el directorio actual.
with open('movies.csv',mode='r', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        print(fila)