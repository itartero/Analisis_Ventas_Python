# Lo primero, importamos las librerias necesarias
from libraries.external import *
from libraries.functions import *
import sys

# Iniciamos la visualización dando la bienvenida al usuario
print("\nBienvenido al aplicativo 'Analisis Ventas Python'")

# Diccionario generado con datos aleatorios mediante Gemini
ventas_dic = {'fecha': ['2026-01-13', '2026-01-20', '2026-02-14', '2026-03-02', '2026-03-24', '2026-04-05', '2026-04-18', '2026-05-11', '2026-05-29', 
'2026-06-03', '2026-06-22', '2026-07-04', '2026-07-19', '2026-08-01', '2026-08-15', '2026-08-28', '2026-09-09', '2026-09-21', '2026-10-03', '2026-10-17'], 
'producto': ['Bidón térmico para ciclismo 750ml', 'Gafas de natación antivaho', 'Botas de tacos multisuperficie', 'Cuerda de saltar de velocidad', 
'Culotte con badana de gel', 'Bandas elásticas de resistencia', 'Espinilleras transpirables', 'Mancuernas hexagonales 10kg', 'Pala de pádel control carbono', 
'Casco aerodinámico ventilado', 'Bicicleta de montaña 29"', 'Raqueta de tenis grafito', 'Bañador de competición hidrofóbico', 'Zapatillas running amortiguación', 
'Camiseta técnica transpirable', 'Pantalón corto deportivo', 'Esterilla yoga antideslizante', 'Cinta de correr plegable', 'Calcetines antiampollas (pack 3)', 
'Balón de fútbol FIFA Pro'], 
'categoria': ['Ciclismo', 'Natación', 'Fútbol', 'Fitness', 'Ciclismo', 'Fitness', 'Fútbol', 'Fitness', 'Tenis / Pádel', 'Ciclismo', 'Ciclismo', 
'Tenis / Pádel', 'Natación', 'Running', 'Running', 'Running', 'Fitness', 'Fitness', 'Running', 'Fútbol'], 
'unidades': [13, 15, 8, 11, 6, 3, 10, 1, 12, 7, 2, 4, 14, 9, 5, 8, 2, 1, 10, 14], 
'precio_unitario': [11.0, 18.5, 79.5, 9.99, 59.9, 15.9, 14.99, 45.0, 95.0, 49.99, 550.0, 119.0, 38.0, 89.9, 19.95, 22.0, 24.99, 450.0, 12.5, 29.99]}

# Ejecutamos la función de 'external.py' que convierte el diccionario en un .csv y lo almacena en /resources
generar_csv(ventas_dic)

# Iniciamos una gestión de errores y ejecutamos la funcion de 'external.py' que nos permite generar el dataframe del .csv recien creado con la ruta destino
try:
    ventas_csv = lectura_csv("resources/ventas.csv")
    print("\nEl archivo csv ha sido correctamente cargado")

# Si la ruta no es válida muestra la causa e interrumpe el programa
except:
    print("\nNo se encuentra el archivo solicitado\n")
    sys.exit()

# Declaramos la variable 'menu_inicio' para iniciar el bucle while que lo mantendrá en activo hasta que el usuario seleccione '4. Salir del programa'
menu_inicio = 0
try:
    # Iniciamos el bucle con la condición de que el usuario no pulse "4"
    while int(menu_inicio) != 4:
        # Consultamos al usuario la función que desea realizar mostrandole un pequeño menú
        menu_inicio = input("\n1. Vista general\n2. Consultar categoria\n3. Generar, archivar y visualizar archivo .parquet\n4. Salir del programa\n\nIntroduzca el número de la función a ejecutar: ")

        # Si el usuario introduce "1" ejecutamos 'calcula_importe()' de la librería 'functions.py'
        if int(menu_inicio) == 1:
            calcula_importe(ventas_csv)

        # Si el usuario introduce "2" ejecutamos 'consulta_categoria()' de la librería 'functions.py'
        elif int(menu_inicio) == 2:
            consulta_categoria(ventas_csv)

        # Si el usuario introduce "3" ejecutamos 'generar_parquet()' de la librería 'external.py'
        elif int(menu_inicio) == 3:
            generar_parquet(ventas_csv)
    
        # Si el usuario selecciona "4" el programa finaliza con el mensaje de despedida
        elif int(menu_inicio) == 4:
            pass

        # Cualquier otro input del usuario devuelve un string
        else:
            print("\nFunción no existente. Introduzca un número válido")

except:
    print("\nEl valor introducido no es válido")

# Mensaje de despedida
print("\n¡Gracias por utilizar Analisis de Ventas con Python!\n")