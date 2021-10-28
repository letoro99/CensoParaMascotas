#!C:\Users\atgma\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
import cgi, os, time
import cgitb; cgitb.enable(display=0, logdir='.')
from dataBase import CensoDatabase
from io import TextIOWrapper
from stat import * 
import re

def validarDB(x):
    return validar_domicilio(x) and validar_fotos(x) and validar_mascota(x) and validar_usuario(x) 


def validar_domicilio(x):
    datos = [x['region'].value, x['comuna'].value, x['calle'].value, x['numero'].value, x['sector'].value]
    for i in range(len(datos)-1):
        if datos[i] == "":
            return False
    if not datos[2].replace(" ","a").isalnum() or not datos[3].isdigit():
        return False
    if 250 < len(x['calle'].value) or 20 < len(x['numero'].value):
        return False
    if datos[4] != "" and not datos[4].replace(" ","a").isalnum():
        return False
    return True

def validar_usuario(x):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    datos = [x['nombre'].value, x['correo'].value, x['celular'].value]
    for i in range(len(datos)-1):
        if datos[i] == "":
            return False
    if 250 < len(datos[0]):
        return False
    if not datos[0].replace(" ","a").isalpha():
        return False
    if datos[2] != "" and not datos[2][1:].isdigit() and not len(datos[2][1:]) == 11:
        return False
    if not re.match(expresion_regular,datos[1]):
        return False
    return True

def validar_mascota(x):
    contador = 0
    while "tipo-mascota"+str(contador) in x:
        datos = [x['tipo-mascota'+str(contador)].value, x['edad-mascota'+str(contador)].value,
                x['color-mascota'+str(contador)].value, x['raza-mascota'+str(contador)].value,
                x['esterilizado-mascota'+str(contador)].value, x['vacunas-mascota'+str(contador)].value
        ]
        for i in range(len(datos)):
            if datos[i] == "":
                return False
        if not datos[0].isdigit() or not datos[4].isdigit() or not datos[5].isdigit() or not datos[1].isdigit():
            return False
        if not datos[2].replace(" ","a").isalpha() or not datos[3].replace(" ","a").isalpha():
            return False
        if 30 < len(datos[2]) or 30 < len(datos[3]):
            return False
        contador += 1
    return True

def validar_fotos(x):
    max_size = 2000000
    extensiones = ['.jpg','.png']
    contador_mascota = 0
    while "tipo-mascota"+str(contador_mascota) in x:
        contador_foto = 0
        while "foto-mascota-"+str(contador_mascota)+str(contador_foto) in x:
            archivo = x['foto-mascota-'+str(contador_mascota)+str(contador_foto)]
            if archivo.value == "" or not archivo.filename.lower()[-4:] in extensiones:
                return False
            tamaño = os.fstat(archivo.file.fileno()).st_size
            if tamaño > max_size:
                return False
            contador_foto+=1
        contador_mascota+=1
    return True
