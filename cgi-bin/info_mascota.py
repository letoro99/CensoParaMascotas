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
id_domicilio = int(form["id"].value)
valores = {1:'Si', 2:'No', 3:'No aplica'}

if "id" in form:
    domicilio = censo_db.get_domicilio_id(id_domicilio)
    comuna = censo_db.get_comuna_id(int(domicilio[0][2]))
    region = censo_db.get_region_id(int(domicilio[0][2]))
    region = censo_db.get_nregion_id(int(region[0][0]))
    head = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Información</title>
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
<div class="titulo_form">Datos del/a dueñ@ y su(s) mascotas</div>
<div class="botones-home">
    <a href="listado_mascota.py?pag=0">Regresar al listado</a>
    <a href="index.py">Página Principal</a>
</div>
    '''
    body1 = f'''
<div class="main-info">
        <div id="domicilio">
            <div class="leyenda_principal">Domicilio</div>

            <div class="entrada">
                <div class="leyenda">Región</div>
                <div class="entrada-info">{str(region)[3:-4]}</div>
            </div>

            <div class="entrada">
                <div class="leyenda">Comuna</div>
                <div class="entrada-info">{str(comuna)[3:-4]}</div>
            </div>

            <div class="entrada">
                <div class="leyenda">Calle</div>
                <div class="entrada-info">{str(domicilio[0][3])}</div>
            </div>

            <div class="entrada">
                <div class="leyenda">Número</div>
                <div class="entrada-info">{str(domicilio[0][4])}</div>
            </div>

            <div class="entrada">
                <div class="leyenda">Sector</div>
                <div class="entrada-info">{str(domicilio[0][5])}</div>
            </div>
        </div>

        <div id="contacto">
            <div class="leyenda_principal">Datos de contacto</div>

            <div class="entrada">
                <div class="leyenda">Nombre</div>
                <div class="entrada-info">{str(domicilio[0][6])}</div>
            </div>

            <div class="entrada">
                <div class="leyenda">Correo electrónico</div>
                <div class="entrada-info">{str(domicilio[0][7])}</div>
            </div>

            <div class="entrada">
                <div class="leyenda">Número de celular</div>
                <div class="entrada-info">{str(domicilio[0][8])}</div>
            </div>
        </div>
        '''
    mascotas = censo_db.get_mascotas_domicilio(id_domicilio)
    print(head)
    print(body1)
    contador = 0
    for mascota in mascotas:
        contador += 1
        tipo = censo_db.get_tipo_id(int(mascota[1]))
        body2 = f'''
        <div id="mascota">
            <div class="leyenda_principal">Información de la mascota n°{str(contador)}</div>

            <div class="entrada">
                <div class="leyenda">Tipo</div>
                <div class="entrada-info">{str(tipo)[3:-4]}</div>
            </div>

            <div class="entrada">
                <div class="leyenda">Edad en años</div>
                <div class="entrada-info">{str(mascota[2])}</div>
            </div>

            <div class="entrada">
                <div class="leyenda">Color</div>
                <div class="entrada-info">{str(mascota[3])}</div>
            </div>

            <div class="entrada">
                <div class="leyenda">Raza</div>
                <div class="entrada-info">{str(mascota[4])}</div>
            </div>

            <div class="entrada">
                <div class="leyenda">Esterilizado</div>
                <div class="entrada-info">{valores[mascota[5]]}</div>
            </div>

            <div class="entrada">
                <div class="leyenda">Vacunas al día</div>
                <div class="entrada-info">{valores[mascota[6]]}</div>
            </div>        
        '''
        print(body2)
    body4 = '''
        <div class="entrada">
            <div class="leyenda_principal">Fotos mascotas</div>        
        '''
    print(body4)
    fotos = censo_db.get_foto(mascotas[0][0])
    for foto in fotos:
        body6 = f'''
            <div class="img-raton">
            <img alt="foto{mascota[0]}" src="{foto[1]}" width="320" height="240">
            </div>
            <br>  
        '''
        print(body6)
    body5 = f'''
        </div>
        </div>
        <div class="botones-home">
            <a href="listado_mascota.py?pag=0">Regresar a listado de mascotas</a>
            <a href="index.py">Página Principal</a>
        </div>
        </body>
        </html>        
        '''
    print(body5)
else:
    pass