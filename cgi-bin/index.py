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

data = censo_db.get_5()

if len(data) > 0:
    head = '''
<!DOCTYPE html>
<!--suppress ALL -->
<html>
<head>
    <meta charset="UTF-8">
    <title>Portada</title>
    <link rel="stylesheet" type="text/css" href="tarea1.css">
    <link rel="stylesheet" type="text/css" href="../libraries/leaflet.css">
    <script src="tarea1.js"></script>
    <script src="script_ajax_mapa.js"></script>
    <script src="../libraries/leaflet.js"></script>
    <script type="text/javascript" scr="coordenadas.json"></script>
</head>
<body onload="init_mapa()">
<div class="cabecera">
    <div class="titulo"><a href="index.py">Censo de mascotas</a></div>
    <div class="menu_principal_fondo">
        <a href="../tarea1_formulario.html">Informar mascotas</a>
        <a href="listado_mascota.py?pag=0">Ver listado de mascotas</a>
        <a href="../tarea1_estadistica.html">Estadísticas</a>
    </div>
    </div>
<div class="cuerpo">
<div class="titulo_form">Bienvenid@s</div>
    <div class="men-bienvenida">Bienvenidos al Censo de mascotas, página diseñada para tener una información
    de todas las mascotas del país.
    <br><br> Puedes ingresar a Informar mascota para poder registrar tus mascotas.
        <br><br> Puedes ingresar a Ver listado de mascotas para ver las últimas 5 mascotas registradas.
        <br><br> Puedes ingresar a Estadísitca para ver la información registrada en nuestra página.
    </div>
    </div>
    <div class="titulo_form">Condiciones de usos</div>
    <div class="men-bienvenida">
    Se espera que cumpla las siguientes condiciones al enviar navegar por la página web:<br><br>
    - Las fotos enviadas esten en el formato .png, .jpg o .jpeg, además de poseer la autoría de estas.<br><br>
    - No ingresar información que puede causar un daño a tercero.<br><br>
    - No utilizar la información obtenida en la página web para fines maliciosos.<br><br>
    </div>
    </div>
    '''
    body1 = '''
<div class="titulo_form">Últimas mascotas inscritas</div>
    <div class="main">
<table>
    <tr>
        <th>Comuna</th>
        <th>Calle</th>
        <th>Tipo - Cantidad</th>
        <th>Foto</th>
    </tr>
    '''
    print(head)
    print(body1)
    for d in data:
        data_mascotas = censo_db.get_mascotas_domicilio(d[0])
        data_fotos = censo_db.get_foto(data_mascotas[0][0])
        comuna = str(censo_db.get_comuna_id(d[2]))
        fila = f'''
        <tr>
            <td>{comuna[3:-4]}</td>
            <td>{str(d[3])}</td>
        '''
        print(fila)
        lista_mascotas = {}       
        for i in data_mascotas:
            i = str(censo_db.get_tipo_id(i[1]))
            i = i[3:-4]
            if i in lista_mascotas:
                lista_mascotas[i] += 1 
            else:
                lista_mascotas[i] = 1
        fila2 = '<td>'
        for tipo in lista_mascotas:
            fila2 += f'{tipo} = {lista_mascotas[tipo]}<br>'
        fila2 += '</td>'
        fila3 = '<td><div class="mas_imagenes">'
        print(fila2)
        for foto in data_fotos:
            fila3 += f'<img width="160" height="120" src="{str(foto[1])}"><br>'
        fila3 += '</div></td></tr>'
        print(fila3)
    body3 = '''
    </table>
    <div class="titulo_form">Mapa con las mascotas inscritas</div>
    <div class="men-bienvenida">Haz click en la mascota si quieres ver toda su información</div>
    <div id="contenedor_mapa"></div>
    </body>
    </html>
    '''
    print(body3)
else:
    html = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Portada</title>
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
<div class="cuerpo">
<div class="titulo_form">Bienvenid@s</div>
    <div id="men-bienvenida">Bienvenidos al Censo de mascotas, página diseñada para tener una información
    de todas las mascotas del país.
    <br><br> Puedes ingresar a Informar mascota para poder registrar tus mascotas.
        <br><br> Puedes ingresar a Ver listado de mascotas para ver las últimas 5 mascotas registradas.
        <br><br> Puedes ingresar a Estadísitca para ver la información registrada en nuestra página.
    </div>
    

    <div class="titulo_form">Últimas mascotas inscritas</div>
    <div id="men-bienvenida">No se han registrado ninguna mascota, ¡Puedes ser el/la primero/a!
    <div class="titulo_form">Condiciones de usos</div>
    <div id="men-bienvenida">
    Se espera que cumpla las siguientes condiciones al enviar navegar por la página web:<br><br>
    - Las fotos enviadas esten en el formato .png, .jpg o .jpeg, además de poseer la autoría de estas.<br><br>
    - No ingresar información que puede causar un daño a tercero.<br><br>
    - No utilizar la información obtenida en la página web para fines maliciosos.<br><br>
    </div>
    </div>
    </body>
    </html>
    '''
    print(html)

