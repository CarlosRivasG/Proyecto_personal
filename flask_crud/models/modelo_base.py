import os

from flask_crud.config.mysqlconnection import connectToMySQL
from flask import flash

class ModeloBase():

    

    @classmethod
    def validar_existe(cls, campo, valor):
        query = f"SELECT count(*) as contador FROM {cls.modelo} WHERE {campo} = %({campo})s;"
        data = { campo : valor }
        results = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        return results[0]['contador'] > 0

    @classmethod
    def get_all(cls):
        query = f"Select p.*, u.nombre as nombre_usuario, count(c.producto_id) as numero_kg FROM productos p JOIN usuarios u ON u.id = p.usuario_id LEFT JOIN cantidades c ON c.producto_id = p.id group by p.id"
        results = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query)
        all_data = []
        for data in results:
            all_data.append(cls(data))
        return all_data


    @classmethod
    def producto(cls, id):
        query = f"SELECT * FROM {cls.modelo} WHERE id = %(id)s"
        data = { 'id' : id }
        
        results = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        print(results)
        return cls(results[0])


    @classmethod
    def delete(cls,data):
        query = f"DELETE FROM productos WHERE id = %(id)s;"
        
        resultado = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado      
        



    @classmethod
    def save(cls, data):

        campos_header = ''
        campos_datos = ''
        for campo in cls.campos:
            campos_header += campo + ','
            campos_datos += f'%({campo})s,'

        query = f"""
                INSERT INTO {cls.modelo} ({campos_header}created_at, updated_at)
                VALUES ({campos_datos} NOW(), NOW());
                """
        resultado = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado


    @staticmethod
    def validar_largo(data, campo, largo):
        is_valid = True
        if len(data[campo]) <= largo:
            flash(f'El largo del {campo} no puede ser menor o igual {largo}', 'error')
            is_valid = False
        return is_valid
    
    @staticmethod
    def validar_cantidad(data, campo, valor):
        is_valid = True
        
        if int(data[campo]) <= valor:
            flash(f"El valor no puede ser 0", "error")
            is_valid = False
        return is_valid