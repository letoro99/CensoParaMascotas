#!C:\Users\atgma\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
import cgi, os
import cgitb; cgitb.enable(display=0, logdir='.')
from dataBase import CensoDatabase
from validadorDB import *
import sys
import datetime
from io import TextIOWrapper

sys.stdout = TextIOWrapper(sys.stdout.buffer.detach(), encoding='utf8')

print("Content-type: text/html; charset=utf-8")
form = cgi.FieldStorage()

censo_db = CensoDatabase("root","")

if validarDB(form) == True:
    if "reg"+"ion" in form:

        data_region = form['region'].value
        data_comuna = str(form['comuna'].value)
        comuna_id = censo_db.get_id_comuna('comuna',data_region,data_comuna)
        fecha = datetime.datetime.now()

        data_domicilio = (fecha, comuna_id, form['calle'].value, form['numero'].value, form['sector'].value, form['nombre'].value, form['correo'].value, form['celular'].value)

        censo_db.save_data_domicilio(data_domicilio)
        id_domicilio = censo_db.get_id_domicilio('domicilio',fecha)
        id_domicilio = id_domicilio[0][0]
        
        contador_mascotas = 0
        while 'tipo-mascota' + str(contador_mascotas) in form:
            tipo = form['tipo-mascota' + str(contador_mascotas)].value
            if tipo == "9":
                tipo = (str(form['tipo-mascota9' + str(contador_mascotas)].value),)
                censo_db.save_tipo(tipo)
                tipo_id = int(censo_db.get_id_tipo(tipo[0]))
            else:
                tipo_id = int(tipo)

            data_mascotaDom = (
                tipo_id, form['edad-mascota'+str(contador_mascotas)].value, form['color-mascota'+str(contador_mascotas)].value,
                form['raza-mascota'+str(contador_mascotas)].value, form['esterilizado-mascota'+str(contador_mascotas)].value,
                form['vacunas-mascota'+str(contador_mascotas)].value, id_domicilio
            )

            censo_db.save_data_mascotaDom(data_mascotaDom)
            id_mascota = censo_db.get_id_mascota('mascota_domicilio',id_domicilio)
            id_mascota = id_mascota[0][0]
                    
            contador_fotos = 0
            while 'foto-mascota-'+str(contador_mascotas)+str(contador_fotos) in form:
                filename = ''
                foto = form['foto-mascota-'+str(contador_mascotas)+str(contador_fotos)]
                filename = foto.filename
                file_path, file_extension = os.path.splitext(filename)
                if file_extension.lower() == '.png' or file_extension.lower() == '.jpg':
                    fn = 'animales/'+str(id_mascota)+str(contador_mascotas)+str(contador_fotos)+file_extension
                    open(fn,'wb').write(foto.file.read())
                    data_foto_mascota = (
                            fn, filename, id_mascota
                    )
                    censo_db.save_data_foto(data_foto_mascota)
                    contador_fotos += 1
                else:
                    html = f'''
                                <!DOCTYPE html>
                                <html>
                                <head>
                                    <meta charset="UTF-8">
                                    <title>Error</title>
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
                                <div class="titulo_form">Error en el formulario enviado!</div>
                                <div class="titulo">Uno de los archivos que se ha enviado posee una extensión no valida. Por favor tratar de usar las extensiones solicitadas</div>
                                <div class="botones-home">
                                <a href="index.py">Volver a la la portada</a>
                                </div>
                                </body>
                                </html>
                                '''
                    print(html)
            contador_mascotas += 1
        html = '''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Recibido!</title>
            <link rel="stylesheet" type="text/css" href="../tarea1.css">
            <script src="../tarea1.js"></script>
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
        <div class="titulo_form">Informacion recibida con exito!</div>
        <div class="titulo">Gracias por tu colaboracion!</div>
         <div class="botones-home">
            <a href="index.py">Volver a la la portada</a>
        </div>
        </body>
        </html>     
        '''
        print(html)
    else:
        html='''
                        <!DOCTYPE html>
                        <html>
                        <head>
                            <meta charset="UTF-8">
                            <title>Error</title>
                            <link rel="stylesheet" type="text/css" href="tarea1.css">
                            <script src="tarea1.js"></script>
                        </head>
                        <body>
                        <div class="cabecera">
                            <div class="titulo"><a href="index.py">Censo de mascotas</a></div>
                            <div class="menu_principal_fondo">
                                <a href="../tarea1_formulario.html">Informar mascotas</a>
                                <a href="listado_mascotas.py?pag=0">Ver listado de mascotas</a>
                                <a href="../tarea1_estadistica.html">Estadísticas</a>
                            </div>
                            </div>
                        <div class="titulo_form">¡Error en el formulario enviado!</div>
                        <div class="titulo">EL formulario enviado se encuentra vacio. Por favor intentarlo nuevamente.</div>
                        <div class="botones-home">
                            <a href="index.py">Volver a la la portada</a>
                        </div>
                        </body>
                        </html>
            '''
        print(html)
else:
    html=f'''
                        <!DOCTYPE html>
                        <html>
                        <head>
                            <meta charset="UTF-8">
                            <title>Error</title>
                            <link rel="stylesheet" type="text/css" href="tarea1.css">
                            <script src="tarea1.js"></script>
                        </head>
                        <body>
                        <div class="cabecera">
                            <div class="titulo"><a href="index.py">Censo de mascotas</a></div>
                            <div class="menu_principal_fondo">
                                <a href="../tarea1_formulario.html">Informar mascotas</a>
                                <a href="listado_mascotas.py?pag=0">Ver listado de mascotas</a>
                                <a href="../tarea1_estadistica.html">Estadísticas</a>
                            </div>
                            </div>
                        <div class="titulo_form">¡Error en el formulario enviado!</div>
                        <div class="titulo">Unos de los datos o archivos son incorrectos, por favor revisar los datos enviados.</div>
                        <div class="botones-home">
                            <a href="index.py">Volver a la la portada</a>
                        </div>
                        </body>
                        </html>
            '''
    print(html)
