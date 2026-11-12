# Este archivo contiene una libreria de funciones inerentes al programa para realizar diversas acciones y calculos
# Primero importamos las librerias necesarias
import pandas as pd

# Función que añade y muestra 'Importe Total', 'Unidades Totales' y una tabla referencial con las ventas por categoría
def calcula_importe(ventas_csv):
    # Creamos el atributo 'importe' y formulamos su valor
    ventas_csv["importe"] = ventas_csv["unidades"] * ventas_csv["precio_unitario"]
    # Creamos las visualizaciones
    print(f"\nImporte Total: {sum(ventas_csv["importe"])} euros")
    print(f"\nCon {sum(ventas_csv["unidades"])} unidades vendidas")
    print("\n", ventas_csv.groupby("categoria")["importe"].sum())

# Esta función devuelve el importe sumado de todas las entradas con un mismo valor 'categoria' seleccionada por el usuario
def consulta_categoria(ventas_csv):
    # Para generar el menu decido utilizar un diccionario para almacenar 'valor' (key) + 'categoria' (value)
    # Comenzamos declarando un contador y el diccionario
    contador = 1
    cat_dic = {}
    # Iniciamos un bucle que itere por las categorias unicas del dataframe en cada bucle se almacena 'contador' como key y la categoria como value, sumando +1 al contador
    for cat in ventas_csv["categoria"].unique():
        cat_dic[contador] = cat
        contador += 1
    # Mostramos el diccionario al usuario
    print(f"\n{cat_dic}")
    
    # Generamos una variable input para seleccionar la categoria requerida
    eleccion_cat = input("\nSelecciona el número de la categoria a consultar: ")
    try:
        # Condicionamos si el numero seleccionado esta dentro del diccionario
        if int(eleccion_cat) in cat_dic.keys():
            # Creamos la variable que alojará la suma del importe
            total_categoria = 0
            # Iteramos en cada una de las lineas del dataframe con el atributo .values de Pandas para dataframes
            for linea in ventas_csv.values:
                # Si la categoria en el index 2 es igual a la categoria introducida por el usuario, suma el importe (precio_unitario * unidades)
                if linea[2] == cat_dic[int(eleccion_cat)]:
                    total_categoria += linea[3] * linea[4]
            # Se muestra la info con un f-string
            print(f"\nEl importe total de {cat_dic[int(eleccion_cat)]} es {total_categoria:.2f} euros")
        else:
            # Si la categoría no existe informa al usuario
            print(f"\nIntroduzca un número correspondiente a una categoría")
    except:
        print("\nEl valor introducido no es válido")