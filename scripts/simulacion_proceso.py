import random
import time
import mysql.connector

def conectar():
    return mysql.connector.connect(
        user='monitor',
        password='moni-tor-1-2-3-4',
        host='localhost',
        database='monitorizacion_procesos',
        port=3306,
        connection_timeout=5
    )

conexion = conectar()
print(conexion)

mycursor = conexion.cursor()

insertar = "INSERT INTO datos_proceso (temperatura, presion, caudal, ph, concentracion, conversion, nivel) VALUES (%s, %s, %s, %s, %s, %s, %s)"

temp1 = 40
temp2 = 70

presion1 = 1.0
presion2 = 2.5

caudal1 = 80
caudal2 = 120

ph1 = 6.5
ph2 = 7.5

cA1 = 1.5
cA2 = 4

conver1 = 80
conver2 = 98

nivel1 = 60
nivel2 = 80


def generar_valor(normal_min, normal_max, alerta_baja_min, alerta_baja_max, alerta_alta_min, alerta_alta_max, alerta=False):

    if alerta:
        if random.random() < 0.5:
            return random.uniform(alerta_baja_min, alerta_baja_max)
        else:
            return random.uniform(alerta_alta_min, alerta_alta_max)

    return random.uniform(normal_min, normal_max)


contador = 0


while True:

    print("Generando nuevos valores...")

    contador += 1

    variable_alerta = None

    if contador % 15 == 0:
        variable_alerta = random.choice([
            "temperatura",
            "presion",
            "caudal",
            "ph",
            "concentracion",
            "conversion",
            "nivel"
        ])

    temp = generar_valor(temp1, temp2, 20, 35, 75, 90, variable_alerta == "temperatura")
    print(temp)

    presion = generar_valor(presion1, presion2, 0.5, 0.9, 3.0, 4.0, variable_alerta == "presion")
    print(presion)

    caudal_de_entrada = generar_valor(caudal1, caudal2, 50, 70, 130, 160, variable_alerta == "caudal")
    print(caudal_de_entrada)

    pH = generar_valor(ph1, ph2, 4.5, 6.0, 8.0, 9.0, variable_alerta == "ph")
    print(pH)

    concentracion = generar_valor(cA1, cA2, 0, 1.49, 4.51, 6.0, variable_alerta == "concentracion")
    print(concentracion)

    conver = generar_valor(conver1, conver2, 60, 75, 98.1, 100, variable_alerta == "conversion")
    print(conver)

    nivel = generar_valor(nivel1, nivel2, 30, 50, 85, 100, variable_alerta == "nivel")
    print(nivel)

    try:
        mycursor.execute(
            insertar,
            (temp, presion, caudal_de_entrada, pH, concentracion, conver, nivel)
        )

        conexion.commit()

        print(mycursor.rowcount, "registro agregado.")

    except mysql.connector.Error as e:
        print("Error MySQL:", e)

        try:
            print("Reconectando a la base de datos...")

            conexion = conectar()
            mycursor = conexion.cursor()

            print("Reconexión correcta")

        except Exception as e2:
            print("No se pudo reconectar:", e2)

    time.sleep(10)