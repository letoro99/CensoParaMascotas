#!C:\Users\atgma\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
import cgi, os
import cgitb; cgitb.enable(display=0, logdir='.')
from dataBase import CensoDatabase
import sys
import datetime
from io import TextIOWrapper

print("Content-type: text/html; charset=utf-8")
form = cgi.FieldStorage()
censo_db = CensoDatabase("root","")

# Pagina principal de la web

pag = int(form['pag'].value)
if pag < 0:
    pag = 0
data = censo_db.get_5_offset(pag*5)

if len(data) > 0 and "pag" in form:
    head = '''
<!DOCTYPE html>
<!--suppress ALL -->
<html>
<head>
    <meta charset="UTF-8">
    <title>Listado de Mascotas</title>
    <link rel="stylesheet" type="text/css" href="tarea1.css">
    <script src="tarea1.js"></script>
</head>
<body>
<div class="cabecera">
    <div class="titulo"><a href="index.py">Censo de mascotas</a></div>
    <div class="menu_principal_fondo">
        <a href="../tarea1_formulario.html">Informar mascotas</a>
        <a href="listado_mascota.py?pag=0">Ver listado de mascotas</a>
        <a href="../tarea1_estadistica.html">Estadísticas</a>
    </div>
    </div>
    '''
    body1 = '''
<div class="titulo_form">Listado de las mascotas inscritas</div>
<div class="main">
<form id="id_mascota" method="GET" action="" enctype="multipart/form-data">
<table>
    <tr>
        <th>Fecha<br>ingreso</th>
        <th>Comuna</th>
        <th>Dirección</th>
        <th>Nombre<br>contacto</th>
        <th>Total<br>mascotas</th>
        <th>Total fotos</th>
    </tr>
    '''
    print(head)
    print(body1)
    num = 0
    for d in data:
        num += 1
        data_mascotas = censo_db.get_mascotas_domicilio(d[0])
        data_fotos = censo_db.get_foto(data_mascotas[0][0])
        comuna = str(censo_db.get_comuna_id(d[2]))
        fila = f'''
        <tr id="{str(num)}" class="info" onclick=redirrection("info_mascota.py?id={str(d[0])}")>
            <td>{str(d[1])}</td>
            <td>{comuna[3:-4]}</td>
            <td>{str(d[3])}</td>
            <td>{str(d[6])}</td>
            <td>{str(len(data_mascotas))}</td>
            <td>{str(len(data_fotos))}</td>
        </tr>
        '''
        print(fila)
    body4 = f'''
    </table>
    </form>
    </div>'''
    if pag != 0:
        body8 = f'''
        <div class="botones-home">
            <a href="listado_mascota.py?pag={pag-1}">Página anterior</a>
            <a href="listado_mascota.py?pag={pag+1}">Siguiente página</a>
        </div>        
        '''
    else:
        body8 = f'''
        <div class="botones-home">
            <a href="listado_mascota.py?pag={pag+1}">Siguiente página</a>
        </div>        
        '''      
    body9 = '''
    </body>
    </html>
    '''
    print(body4)
    print(body8)
    print(body9)
else:
    html = f'''
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Error!!</title>
                <link rel="stylesheet" type="text/css" href="tarea1.css">
                <script src="tarea1.js"></script>
            </head>
            <body>
            <div class="cabecera">
                <div class="titulo"><a href="index.py">Censo de mascotas</a></div>
                <div class="menu_principal_fondo">
                    <a href="../tarea1_formulario.html">Informar mascotas</a>
                    <a href="listado_mascota.py?pag=0">Ver listado de mascotas</a>
                    <a href="../tarea1_estadistica.html">Estadísticas</a>
                </div>
                </div>
            <div class="titulo_form">¡Error en la página!</div>
            <div class="titulo">No se encuentran más mascotas registradas</div>
            <div class="botones-home">
                <a href="listado_mascota.py?pag={pag-1}">Página anterior</a>
                <a href="index.py">Volver a la la portada</a>
            </div>
            </body>
            </html>
    '''
    print(html)

