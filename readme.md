# Análisis de Ventas con Python
**Documentación técnica y memoria del proyecto**

---

## 1. Arquitectura y organización del proyecto

El programa está estructurado en el archivo `main.py`, el cual controla el flujo de ejecución y las interacciones con el usuario, acompañado de dos subcarpetas principales:

- **`/libraries`**: contiene dos módulos propios:
  - **`external.py`**: incluye funciones dedicadas exclusivamente a la entrada y salida de datos.
  - **`functions.py`**: alberga las funciones dedicadas a la analítica mediante cálculos, agrupaciones y consultas.
- **`/resources`**: aloja los archivos dependientes del programa (`ventas.csv` y `ventas_procesadas.parquet`).

```text
Analisis_Ventas_Python/
│
├─ main.py                       # Punto de entrada y flujo interactivo
├─ libraries/                    # Módulos propios con lógica reutilizable
│   ├─ external.py               # Entrada/Salida (CSV, Parquet)
│   └─ functions.py              # Lógica analítica
├─ resources/                    # Almacenamiento de datos
│   ├─ ventas.csv                # Dataset inicial de ventas
│   └─ ventas_procesadas.parquet # Dataset transformado .parquet
└─ readme.md                     # Documentación y memoria del proyecto
```

Todo el código se encuentra debidamente comentado para facilitar su lectura y comprender su propósito. Esta estructura modular y escalable permite la reutilización de funciones clave en futuros desarrollos.

---

## 2. Circulación de los datos

El flujo de vida de los datos se divide en etapas secuenciales y controladas:

### Definición e inicialización de datos base
- **`main.py`** define un diccionario `ventas_dic` que contiene 20 registros con las keys requeridas: `fecha`, `producto`, `categoria`, `unidades` y `precio_unitario`.
- Se llama a **`generar_csv`**, que valida si `resources/ventas.csv` existe en disco y convierte el diccionario a un CSV.
- **`lectura_csv`** carga el archivo en la memoria como dataset en la variable `ventas_csv`.

### Interacción y procesamiento
- El DataFrame `ventas_csv` se pasa como parámetro a las distintas opciones del menú interactivo ejecutado en un bucle `while` en `main.py`.
- Los `input` de selección del menú están protegidos mediante `try-except`, garantizando que entradas no numéricas o cadenas vacías devuelvan un string en lugar de provocar la detención del script.
- **Opción 1 (`calcula_importe`)**: Añade la columna calculada `importe = unidades * precio_unitario`. Imprime los totales globales (suma de importes y unidades vendidas) y las ventas agrupadas por categoría.
- **Opción 2 (`consulta_categoria`)**: Permite una consulta por categoría seleccionada por el usuario mediante un selector dinámico numerado.

### Exportación a .parquet
- **Opción 3 (`generar_parquet`)**: Toma el dataset `ventas_csv` y lo exporta a `resources/ventas_procesadas.parquet`. Acto seguido, lee el fichero generado en una nueva variable `ventas_parquet` y se muestra en consola.

### Salida controlada
- **Opción 4**: Rompe el bucle de ejecución mediante `pass`, cerrando el programa.

---

## 3. Funcionamiento de la función `consulta_categoria`

La función `consulta_categoria` (ubicada en `libraries/functions.py`) se encarga de aislar, filtrar y sumar las ventas asociadas a una categoría elegida por el usuario:

```python
def consulta_categoria(ventas_csv):
    # Generación dinámica del catálogo de categorías
    contador = 1
    cat_dic = {}
    for cat in ventas_csv["categoria"].unique():
        cat_dic[contador] = cat
        contador += 1
        
    print(f"\n{cat_dic}")

    # Captura controlada del input del usuario
    try:
        eleccion_cat = int(input("\nSelecciona el número de la categoría a consultar: "))
        
        # Validación de rango contra las opciones disponibles
        if eleccion_cat in cat_dic.keys():
            total_categoria = 0
            
            # Recorrido de los registros mediante acceso por posición
            for linea in ventas_csv.values:
                if linea[2] == cat_dic[eleccion_cat]:
                    total_categoria += linea[3] * linea[4]
                    
            print(f"\nEl importe total de {cat_dic[eleccion_cat]} es {total_categoria:.2f} euros")
        else:
            print("\nIntroduzca un número correspondiente a una categoría válida.")
            
    except ValueError:
        print("\nError: Debe introducir un número entero válido.")

        print(f"\nIntroduzca un número correspondiente a una categoría")
```

En su ejecución, comenzamos construyendo el diccionario que servirá de guía para el usuario a la hora de seleccionar una categoría entre las existentes en el archivo CSV. Para ello declaramos una variable `contador` y el diccionario vacío `cat_dic`. El contador generará las diferentes keys e iterando por las categorías únicas presentes en el DataFrame con el método `unique()` de Pandas, generaremos sus respectivos values, iniciando el contador en 1 y sumando una unidad en cada iteración. Terminamos esta parte mostrando este diccionario en consola por ser lo suficientemente claro para el usuario.

Tras ello, solicitamos un número mediante `input` guardándolo en la variable `eleccion_cat`, iniciamos una captura de errores con `try-except` para evitar valores no numéricos y comprobamos si existe en el diccionario `cat_dic`, convirtiendo el valor a entero con el método `int()`, ya que los `input` devuelven strings. De ser válido, declaramos `total_categoria` e iteramos con un bucle `for` sobre las filas del DataFrame usando el atributo `.values`. En cada iteración comprobamos si la categoría coincide y, de ser así, acumulamos el importe (`precio_unitario * unidades`) en `total_categoria`.

Por último, generamos una salida formateada mediante un f-string para mostrar el resultado de forma clara con dos dígitos decimales.

En caso de que el usuario introduzca un valor inexistente, se mostrará un mensaje de advertencia indicando que debe introducir un número asignado válido y, de ser un valor no numérico, capturaremos el error mostrando al usuario un string.

---

## 4. Declaración de uso de Inteligencia Artificial

La utilización de Gemini se realizó mediante un cuaderno de NotebookLM configurado con instrucciones de acompañar pedagógicamente, fomentando el aprendizaje guiado y el razonamiento crítico sin entregar soluciones directas ni código resuelto.

Se recurrió a la herramienta en los siguientes puntos:
- Generación aleatoria de las 20 líneas de datos con las que trabajar en el ejercicio.
- Orientación para resolver la consulta de ventas por categoría introducida por el usuario y evaluar si la categoría existe dentro del DataFrame antes de sumar su importe en la función `consulta_categoria`. A partir de las indicaciones, se corrigió la llamada de `.values()` a `.values` y se evaluó el uso de una máscara booleana con `['importe'].sum()`, descartándola a favor de un bucle `for` por ser una estructura más conocida por el alumno.
- Auditoría del código como árbitro crítico imparcial. Al comprobar que las sugerencias eran de optimización y estilo fuera de temario, se mantuvo el código original para valorar la evolución futura.
- Recopilar las consultas del NotebookLM y convertirlas a formato `README.md` para incluirlo en la memoria.

Todo el código entregado ha sido escrito, revisado y verificado personalmente.

### Registro de ejecución del programa en terminal

```shell
@cloudshell:~/1_Fundamentos_Python/Analisis_Ventas_Python$ python3 main.py

Bienvenido al aplicativo 'Analisis Ventas Python'

El archivo csv ha sido correctamente cargado

1. Vista general
2. Consultar categoria
3. Generar, archivar y visualizar archivo .parquet
4. Salir del programa

Introduzca el número de la función a ejecutar: 1

Importe Total: 7496.01 euros

Con 155 unidades vendidas

 categoria
Ciclismo         1952.33
Fitness           702.57
Fútbol           1205.76
Natación          809.50
Running          1209.85
Tenis / Pádel    1616.00
Name: importe, dtype: float64

1. Vista general
2. Consultar categoria
3. Generar, archivar y visualizar archivo .parquet
4. Salir del programa

Introduzca el número de la función a ejecutar: 2

{1: 'Ciclismo', 2: 'Natación', 3: 'Fútbol', 4: 'Fitness', 5: 'Tenis / Pádel', 6: 'Running'}

Selecciona el número de la categoria a consultar: 5

El importe total de Tenis / Pádel es 1616.00 euros

1. Vista general
2. Consultar categoria
3. Generar, archivar y visualizar archivo .parquet
4. Salir del programa

Introduzca el número de la función a ejecutar: 3

          fecha                            producto      categoria  unidades  precio_unitario  importe
0   2026-01-13   Bidón térmico para ciclismo 750ml       Ciclismo        13            11.00   143.00
1   2026-01-20          Gafas de natación antivaho       Natación        15            18.50   277.50
2   2026-02-14      Botas de tacos multisuperficie         Fútbol         8            79.50   636.00
3   2026-03-02       Cuerda de saltar de velocidad        Fitness        11             9.99   109.89
4   2026-03-24           Culotte con badana de gel       Ciclismo         6            59.90   359.40
5   2026-04-05     Bandas elásticas de resistencia        Fitness         3            15.90    47.70
6   2026-04-18          Espinilleras transpirables         Fútbol        10            14.99   149.90
7   2026-05-11         Mancuernas hexagonales 10kg        Fitness         1            45.00    45.00
8   2026-05-29       Pala de pádel control carbono  Tenis / Pádel        12            95.00  1140.00
9   2026-06-03        Casco aerodinámico ventilado       Ciclismo         7            49.99   349.93
10  2026-06-22            Bicicleta de montaña 29"       Ciclismo         2           550.00  1100.00
11  2026-07-04            Raqueta de tenis grafito  Tenis / Pádel         4           119.00   476.00
12  2026-07-19  Bañador de competición hidrofóbico       Natación        14            38.00   532.00
13  2026-08-01    Zapatillas running amortiguación        Running         9            89.90   809.10
14  2026-08-15       Camiseta técnica transpirable        Running         5            19.95    99.75
15  2026-08-28            Pantalón corto deportivo        Running         8            22.00   176.00
16  2026-09-09       Esterilla yoga antideslizante        Fitness         2            24.99    49.98
17  2026-09-21            Cinta de correr plegable        Fitness         1           450.00   450.00
18  2026-10-03    Calcetines antiampollas (pack 3)        Running        10            12.50   125.00
19  2026-10-17            Balón de fútbol FIFA Pro         Fútbol        14            29.99   419.86

1. Vista general
2. Consultar categoria
3. Generar, archivar y visualizar archivo .parquet
4. Salir del programa

Introduzca el número de la función a ejecutar: 4

¡Gracias por utilizar Analisis de Ventas con Python!
```