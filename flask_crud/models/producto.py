
import os

from flask import flash, session
from flask_crud.config.mysqlconnection import connectToMySQL
from flask_crud.models.modelo_base import ModeloBase


from flask_crud.utils.regex import REGEX_CORREO_VALIDO

class producto(ModeloBase):

    modelo = 'productos'
    campos = ['nombre','precio','numero_kg','descripcion','tipo_producto', 'Usuario_id']

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.numero_kg = data['numero_kg']
        self.precio = data['precio']
        self.descripcion = data['descripcion']
        self.tipo_producto = data['tipo_producto']
        self.Usuario_id = data['Usuario_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    @classmethod
    def save_producto(cls, data):
        query = f"INSERT INTO `stock`.`productos` (`nombre`, `precio`, `descripcion`, `tipo_producto`,`Usuario_id`, `created_at`, `updated_at`) VALUES (%(nombre)s, %(precio)s,%(descripcion)s,%(tipo_producto)s,%(Usuario_id)s,NOW(), NOW());"
        print(query)
        resultado = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado
    
    @classmethod
    def update_producto(cls,data):
        query = """UPDATE productos
                        SET nombre= %(nombre)s, precio = %(precio)s, tipo_producto = %(tipo_producto)s,  
                        descripcion = %(descripcion)s WHERE id =  %(id)s;"""
        print(query)
        resultado = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado



    @classmethod
    def get_by_id_user(cls, id):
        query = f"SELECT * FROM productos JOIN usuarios ON usuarios.id = pinturas.usuario_id WHERE productos.id = %(id)s" 
        data = {'id': id,
        }
        results = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query,data)
        print("AQUI QUIERO VER -->",results)
        all_data = []
        for data in results:
            all_data.append(cls(data))
        return all_data

    @classmethod
    def get_by_id2(cls, id):
        query = f"SELECT productos.*, CONCAT(usuarios.nombre, ' ', usuarios.apellido) AS nombre_usuario  FROM  productos JOIN usuarios  on usuarios.id = usuario_id WHERE usuario_id = %(id)s"
        data = { 'id' : id }
        results = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        print(results)
        return cls(results[0])
    
    @classmethod
    def get_by_id3(cls, id):
        query = f"SELECT  productos.* FROM  productos WHERE  productos.id = %(id)s"
        data = { 'id' : id }
        results = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        print(results)
        return results
    
    @classmethod
    def cantidadpositiva(cls, data):
        query = """
                INSERT INTO cantidades (usuario_id, producto_id)
                VALUES (%(Usuario_id)s, %(producto_id)s);
                """
        resultado = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado

    @classmethod
    def cantidadnegativa(cls, data):
        query = """
                DELETE FROM cantidades WHERE usuario_id =  %(usuario_id)s and producto_id = %(producto_id)s;
                """
        resultado = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado
   

    @classmethod
    def validar_producto(cls, data):

            is_valid = True

            is_valid = cls.validar_largo(data, 'nombre', 2)
            
            is_valid = cls.validar_cantidad(data, 'precio', 0)
            return is_valid

