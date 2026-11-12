# Este archivo contiene una libreria de funciones dedicadas a trabajar con archivos externos con extensiones .csv y .parquet
# Primero importamos las librerias necesarias
import pandas as pd
import sys

# Función que convierte un diccionario en un archivo 'ventas.csv'
def generar_csv(diccionario):
    # Comprueba si las columnas necesarias para todos los calculos posteriores estan presentes, convierte los datos en un dataframe y lo exporta a un .csv
    if 'categoria' in diccionario.keys() and 'unidades' in diccionario.keys() and "precio_unitario" in diccionario.keys():
        df = pd.DataFrame(diccionario)
        df.to_csv("resources/ventas.csv", index = False)
    # En caso de no encontrar las columnas necesaria el progrma se interrumpe
    else:
        print("\nDatos no compatibles\n")
        sys.exit()

# Función que lee un archivo .csv desde una ruta y devuelve un dataframe con la variable 'ventas_csv'
def lectura_csv(ruta_csv):
    ventas_csv = pd.read_csv(ruta_csv)
    return ventas_csv

# Función que exporta un dataframe en un archivo .parquet, lo lee y lo visualiza en la terminal
def generar_parquet(ventas_csv):
    ventas_csv.to_parquet("resources/ventas_procesadas.parquet", index = False)
    ventas_parquet = pd.read_parquet("resources/ventas_procesadas.parquet")
    print("\n", ventas_parquet)