#!C:\Users\atgma\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-

import cgitb; cgitb.enable(display=0, logdir='.')
import codecs
import sys
import mysql.connector
import json
import cgi
import html
from dataBase import CensoDatabase

censo_db = CensoDatabase("root","")
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
cgitb.enable()

print('Content-type: text/html; charset=UTF-8')
print('')

informacion = {}
cantidad = censo_db.get_datos_tabla1()
fecha_inicial = cantidad[0][1].strftime("%d-%m-%Y")
datos,fecha_actual = [],''
k = -1
for i in cantidad:
    fecha = i[1].strftime("%d-%m-%Y")
    if fecha == fecha_actual:
        datos[k][1] += 1
    else:
        datos.append([str(fecha),1])
        k +=1
        fecha_actual = fecha
informacion[0] = datos

cantidad = censo_db.get_datos_tabla2()
cant = [0,0,0,0,0,0,0,0,0]
for i in cantidad:
    indice = int(i[1]) - 1
    if indice > 7:
        cant[8] += 1
    else:
        cant[indice] += 1
informacion[1] = cant

cantidad = censo_db.get_datos_tabla3()
datos = []
meses = []
k=0
for i in cantidad:
    mes = censo_db.get_fecha_domicilio(i[2])
    mes = mes[0][0].strftime('%m-%Y')
    if mes in meses and i[1] == 1:
        datos[meses.index(mes)][0] += 1
    elif mes in meses and i[1] == 2:
        datos[meses.index(mes)][1] += 1
    elif not mes in meses and i[1] == 1:
        meses.append(mes)
        datos.append([1,0])
    elif not mes in meses and i[1] == 2:
        meses.append(mes)
        datos.append([0,1])
informacion[2] = [meses,datos]
print(json.dumps(informacion))