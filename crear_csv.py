import csv

# Escribir datos en un archivo CSV
datos = [["Nombre", "Edad", "País"],
         ["Ana", 28, "España"],
         ["Juan", 35, "México"],
         ["Lucía", 22, "Argentina"]]

with open('salida.csv', mode='w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerows(datos)
