import random
import time
import mysql.connector 

conexion = mysql.connector.connect(user = 'monitor', password = 'moni-tor-1-2-3-4', host = '192.168.1.108', database = 'monitorizacion_procesos', port = '3306')
print (conexion)

mycursor = conexion.cursor()
insertar = "INSERT INTO datos_proceso (temperatura, presion, caudal, ph, concentracion, conversion, nivel) VALUES (%s, %s, %s, %s, %s, %s, %s) "



temp1= 40
temp2= 70
presion1=1.0
presion2=2.5
caudal1= 80
caudal2=120
ph1=6.5
ph2=7.5
cA1=0.0
cA2=5.0
conver1=80
conver2=98
nivel1=60
nivel2=80

while True:
    temp = random.uniform(temp1, temp2)
    print(temp)
    presion = random.uniform(presion1, presion2)
    print(presion)
    caudal_de_entrada = random.uniform(caudal1, caudal2)
    print(caudal_de_entrada)
    pH = random.uniform(ph1,ph2)
    print(pH)
    concentracion = random.uniform(cA1,cA2)
    print(concentracion)
    conver = random.uniform(conver1,conver2)
    print(conver)
    nivel = random.uniform(nivel1,nivel2)
    print(nivel)
    mycursor.execute(insertar,(temp, presion, caudal_de_entrada, pH, concentracion, conver, nivel))
    conexion.commit()
    time.sleep(10)
    print(mycursor.rowcount, "registro agregado.")