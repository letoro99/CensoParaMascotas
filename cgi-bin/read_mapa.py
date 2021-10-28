#!C:\Users\atgma\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-

import cgitb; cgitb.enable(display=0, logdir='.')
import codecs
import sys
import json
import cgi
import html
from dataBase import CensoDatabase

censo_db = CensoDatabase("root","")
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
cgitb.enable()

print('Content-type: text/html; charset=UTF-8')
print('')

datos_fotos_mascotas = censo_db.get_all("foto_mascota")
comunas_mascotas = {}
for i in datos_fotos_mascotas:
    mascota = censo_db.get_mascota_idfoto(i[3])
    comuna_id = censo_db.get_domicilio_id(mascota[0][7])
    comuna_nombre = censo_db.get_comuna_id(comuna_id[0][2])[0][0]
    if not comuna_nombre in comunas_mascotas:
        comunas_mascotas[comuna_nombre] = [[i[1],mascota[0]]]
    else:
        comunas_mascotas[comuna_nombre].append([i[1],mascota[0]])
datos_fotos_mascotas = None
print(json.dumps(comunas_mascotas))


