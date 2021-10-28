#!C:\Users\atgma\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
import mysql.connector

class CensoDatabase:

    def __init__(self,user,password):
        self.db = mysql.connector.connect(
            host = "localhost",
            user = user,
            password = password,
            database = "tarea2"
        )
        self.cursor = self.db.cursor()
    
    def eliminar_tilde(self,palabra):
        acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'Á': 'A', 'E': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}
        for letra in acentos:
            if letra in palabra:
                palabra = palabra.replace(letra,acentos[letra])
        return palabra
    
    def save_data_foto(self,data): # Se debe ocupar, para guardar las fotos al final del todo
        sql = """
        INSERT INTO foto_mascota (ruta_archivo, nombre_archivo, mascota_domicilio_id)
        VALUES (%s,%s,%s)        
        """
        self.cursor.execute(sql,data)
        self.db.commit()

    def save_data_mascotaDom(self,data):  # Se debe ocupar
        sql = '''
            INSERT INTO mascota_domicilio (tipo_mascota_id, edad, color, raza, esterilizado, vacunas_al_dia, domicilio_id)
            VALUE (%s,%s,%s,%s,%s,%s,%s)        
        '''
        self.cursor.execute(sql,data)
        self.db.commit()

    def save_data_domicilio(self,data): # Se debe ocupar
        sql='''
            INSERT INTO domicilio (fecha_ingreso, comuna_id, nombre_calle, numero, sector, nombre_contacto, email, celular)
            VALUE (%s,%s,%s,%s,%s,%s,%s,%s)
        '''
        self.cursor.execute(sql,data)
        self.db.commit()
    
    def save_tipo(self,valor):
        sql = '''
            INSERT INTO tipo_mascota (nombre)
            VALUE (%s)
        '''
        self.cursor.execute(sql,valor)
        self.db.commit()

    def get_all(self,tablename):
        self.cursor.execute(f'SELECT * FROM {tablename}')
        return self.cursor.fetchall()
    
    def get_5(self):
        self.cursor.execute(f'SELECT id, fecha_ingreso, comuna_id, nombre_calle, numero, sector, nombre_contacto, email, celular FROM domicilio ORDER BY fecha_ingreso DESC LIMIT 5')
        return self.cursor.fetchall()
    
    def get_5_offset(self,num):
        self.cursor.execute(f'SELECT id, fecha_ingreso, comuna_id , nombre_calle, numero, sector, nombre_contacto, email, celular FROM domicilio ORDER BY fecha_ingreso DESC LIMIT 5 OFFSET {num}')
        return self.cursor.fetchall()

    def get_mascotas_domicilio(self,valor):
        self.cursor.execute(f'SELECT id, tipo_mascota_id, edad, color, raza, esterilizado, vacunas_al_dia, domicilio_id FROM mascota_domicilio WHERE domicilio_id={valor} ORDER BY id ASC')
        return self.cursor.fetchall()
    
    def get_foto(self,valor):
        self.cursor.execute(f'SELECT id, ruta_archivo, nombre_archivo, mascota_domicilio_id FROM foto_mascota WHERE mascota_domicilio_id = {valor} ORDER BY id ASC')
        return self.cursor.fetchall()

    def get_id_comuna(self,tablename,valor1,valor2):
        self.cursor.execute(f'SELECT * FROM {tablename} WHERE region_id ={valor1}')
        comunas = self.cursor.fetchall()
        comuna_id = '' 
        for i in range(len(comunas)):
            if comunas[i][1] == self.eliminar_tilde(valor2):
                comuna_id = comunas[i][0]
                break
        return comuna_id
    
    def get_id_domicilio(self,tablename,valor):
        self.cursor.execute(f'SELECT id FROM {tablename} ORDER BY id DESC LIMIT 1')
        return self.cursor.fetchall()      

    def get_domicilio_id(self,valor):
        self.cursor.execute(f'SELECT * FROM domicilio WHERE id = {valor}')
        return self.cursor.fetchall()      

    def get_id_tipo(self,valor):
        self.cursor.execute(f'SELECT * FROM tipo_mascota')
        lista = self.cursor.fetchall()
        for i in range(len(lista)):
            if lista[i][1] == valor:
                return lista[i][0]
                break
    
    def get_id_mascota(self,tablename,valor):
        self.cursor.execute(f'SELECT id FROM {tablename} WHERE domicilio_id = {valor}')
        return self.cursor.fetchall()
    
    def get_comuna_id(self,valor):
        self.cursor.execute(f'SELECT nombre FROM comuna WHERE id = {valor}')
        return self.cursor.fetchall()

    def get_region_id(self,valor):
        self.cursor.execute(f'SELECT region_id FROM comuna WHERE id = {valor}')
        return self.cursor.fetchall()

    def get_nregion_id(self,valor):
        self.cursor.execute(f'SELECT nombre FROM region WHERE id = {valor}')
        return self.cursor.fetchall()

    def get_tipo_id(self,valor):
        self.cursor.execute(f'SELECT nombre FROM tipo_mascota WHERE id = {valor}')
        return self.cursor.fetchall()

    def get_datos_tabla1(self):
        sql = '''
            SELECT id, fecha_ingreso FROM domicilio ORDER BY fecha_ingreso
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_datos_tabla2(self):
        sql = '''
            SELECT id, tipo_mascota_id FROM mascota_domicilio
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def get_datos_tabla3(self):
        sql = '''
            SELECT id, tipo_mascota_id, domicilio_id FROM `mascota_domicilio` WHERE tipo_mascota_id = 1 or tipo_mascota_id = 2
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_fecha_domicilio(self,data):
        sql = '''
            SELECT fecha_ingreso FROM domicilio WHERE id = (%s)
        '''
        self.cursor.execute(sql,(data,))
        return self.cursor.fetchall()
    
    def get_mascota_idfoto(self,data):
        sql = '''
            SELECT * FROM mascota_domicilio WHERE id = (%s)
        '''
        self.cursor.execute(sql,(data,))
        return self.cursor.fetchall()
