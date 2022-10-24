import os
from flask import redirect, render_template, request, flash, session
from flask_crud import app
from flask import flash, session,redirect 
from flask_crud.config.mysqlconnection import connectToMySQL
from flask_crud.models.modelo_base import ModeloBase
from flask_crud.models.producto import producto
from flask_crud.utils.regex import REGEX_CORREO_VALIDO


@app.route("/procesar_cantidad/<id>")
def procesar_cantidad(id):

    data = {
        'producto_id' : id,
        'Usuario_id': session['Usuario_id'],
    }

    resultado = producto.cantidadpositiva(data)

    if not resultado and resultado != 0:
        flash("error al aumentar la cantidad", "error")
        return redirect("/Productos")

    flash("cantidad creada", "success")
    return redirect("/Productos")

@app.route("/procesar_cantidad_negativa/<id>")
def procesar_cantidad_negativa(id):

    data = {
        'producto_id' : id,
        'Usuario_id': session['Usuario_id']
    }

    producto.cantidadnegativa(data)

    flash("cantidad eliminada", "success")
    return redirect("/Productos")