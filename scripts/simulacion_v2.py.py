import random                    # Librería para generar números aleatorios
import time                      # Librería para controlar tiempos (sleep)
import mysql.connector           # Librería para conectar Python con MySQL


# CONEXIÓN A LA BASE DE DATOS
conexion = mysql.connector.connect(
    user='monitor',              # Usuario de la base de datos
    password='moni-tor-1-2-3-4', # Contraseña del usuario
    host='localhost',            # Servidor donde está la base de datos
    database='monitorizacion_procesos', # Nombre de la base de datos
    port=3306                    # Puerto de MySQL
)

print(conexion)                  # Muestra en pantalla si la conexión se ha realizado correctamente


mycursor = conexion.cursor()     # Crea un cursor que permite ejecutar consultas SQL


# CONSULTA SQL PARA INSERTAR DATOS
insertar = "INSERT INTO datos_proceso (temperatura, presion, caudal, ph, concentracion, conversion, nivel) VALUES (%s, %s, %s, %s, %s, %s, %s)"


# RANGOS NORMALES DE FUNCIONAMIENTO DEL PROCESO

temp1 = 40                       # Temperatura mínima normal
temp2 = 70                       # Temperatura máxima normal

presion1 = 1.0                   # Presión mínima normal
presion2 = 2.5                   # Presión máxima normal

caudal1 = 80                     # Caudal mínimo normal
caudal2 = 120                    # Caudal máximo normal

ph1 = 6.5                        # pH mínimo normal
ph2 = 7.5                        # pH máximo normal

cA1 = 0.0                        # Concentración mínima normal
cA2 = 5.0                        # Concentración máxima normal

conver1 = 80                     # Conversión mínima normal
conver2 = 98                     # Conversión máxima normal

nivel1 = 60                      # Nivel mínimo normal
nivel2 = 80                      # Nivel máximo normal



# FUNCIÓN PARA GENERAR VALORES NORMALES O ANÓMALOS
def generar_valor(normal_min, normal_max, alerta_baja_min, alerta_baja_max, alerta_alta_min, alerta_alta_max, alerta=False):

    # Si la variable tiene que generar una alerta
    if alerta:

        # Se genera un número aleatorio entre 0 y 1
        if random.random() < 0.5:

            # 50% de probabilidad de generar alerta baja
            return random.uniform(alerta_baja_min, alerta_baja_max)

        else:

            # 50% de probabilidad de generar alerta alta
            return random.uniform(alerta_alta_min, alerta_alta_max)

    # Si no hay alerta se genera un valor normal
    return random.uniform(normal_min, normal_max)



contador = 0                     # Contador que permite saber cuántas iteraciones lleva el programa


while True:                      # Bucle infinito para generar datos continuamente

    contador += 1                # Se incrementa el contador en cada iteración


    variable_alerta = None       # Variable que indicará qué parámetro fallará


    # Cada 15 ciclos se genera una anomalía
    if contador % 15 == 0:

        # Se selecciona aleatoriamente qué variable fallará
        variable_alerta = random.choice([
            "temperatura",
            "presion",
            "caudal",
            "ph",
            "concentracion",
            "conversion",
            "nivel"
        ])



    # GENERACIÓN DE TEMPERATURA
    temp = generar_valor(
        temp1, temp2,             # rango normal
        20, 35,                   # alerta baja
        75, 90,                   # alerta alta
        variable_alerta == "temperatura"  # solo genera alerta si esta variable fue elegida
    )

    print("Temperatura:", temp)   # Muestra el valor generado



    # GENERACIÓN DE PRESIÓN
    presion = generar_valor(
        presion1, presion2,
        0.5, 0.9,
        3.0, 4.0,
        variable_alerta == "presion"
    )

    print("Presion:", presion)



    # GENERACIÓN DE CAUDAL
    caudal_de_entrada = generar_valor(
        caudal1, caudal2,
        50, 70,
        130, 160,
        variable_alerta == "caudal"
    )

    print("Caudal:", caudal_de_entrada)



    # GENERACIÓN DEL PH
    pH = generar_valor(
        ph1, ph2,
        4.5, 6.0,
        8.0, 9.0,
        variable_alerta == "ph"
    )

    print("pH:", pH)



    # GENERACIÓN DE CONCENTRACIÓN
    concentracion = generar_valor(
        cA1, cA2,
        -1.0, -0.2,
        6.0, 8.0,
        variable_alerta == "concentracion"
    )

    print("Concentracion:", concentracion)



    # GENERACIÓN DE CONVERSIÓN
    conver = generar_valor(
        conver1, conver2,
        60, 75,
        99, 105,
        variable_alerta == "conversion"
    )

    print("Conversion:", conver)



    # GENERACIÓN DEL NIVEL
    nivel = generar_valor(
        nivel1, nivel2,
        30, 50,
        85, 100,
        variable_alerta == "nivel"
    )

    print("Nivel:", nivel)



    # EJECUCIÓN DE LA CONSULTA SQL
    mycursor.execute(
        insertar,
        (temp, presion, caudal_de_entrada, pH, concentracion, conver, nivel)
    )


    conexion.commit()            # Guarda los cambios en la base de datos


    print(mycursor.rowcount, "registro agregado.")  # Muestra cuántos registros se han insertado


    time.sleep(10)               # Espera 10 segundos antes de generar el siguiente registro