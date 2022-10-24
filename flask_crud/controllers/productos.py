from flask import redirect, render_template, request, flash, session
from flask_crud import app
from flask_crud.models.producto import producto
from flask_crud.models.usuario import Usuario



@app.route("/panel")
def index():

    return render_template("panel.html")# productos=producto.get_all_productos()

@app.route("/Productos")
def productos():
    if 'usuario' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/login')
        
    
    return render_template("Productos.html", product= producto.get_all() )


@app.route("/producto/<int:id>")
def producto_id(id):
    if 'usuario' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/') 
        
    return render_template("producto.html") #productos=producto.get_by_id2(id)


@app.route("/producto/nueva")
def nueva_producto():

    if 'usuario' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/')

    return render_template("nueva_producto.html")
    


@app.route("/procesar_producto/", methods=["POST"])
def procesar_producto():

    if not producto.validar_producto(request.form):
        return redirect('/panel')

    data = {
        'nombre' : request.form['nombre'],
        
        'precio' : request.form['precio'],
        'tipo_producto' : request.form['tipo_producto'],
        'descripcion' : request.form['descripcion'],        
        'Usuario_id': session['Usuario_id']

    }

    resultado = producto.save_producto(data)
    print(resultado)
    

    if not resultado:
        flash("error al crear la producto", "error")
        return redirect("/producto/nueva")

    flash("producto creado correctamente", "success")
    return redirect("/producto/nueva")

@app.route("/producto/<id>/editar")
def editar(id):
    if 'usuario' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/')

    
    productoss=producto.get_by_id3(id)
    return render_template('edit.html',productos=productoss[0])
    

@app.route("/procesar_actualizacion/<int:id>", methods=["POST"])
def Actualizar_producto(id):
    print(Actualizar_producto)
    if 'usuario' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/')
    
    
    
    actz_producto= {
            "id":id,
            'nombre' : request.form['nombre'],
            
            'precio' : request.form['precio'],
            'tipo_producto' : request.form['tipo_producto'],
            'descripcion' : request.form['descripcion'],        
            'Usuario_id': session['Usuario_id']

    }
          
    if not producto.validar_producto(request.form):
        return redirect('/Productos')
    resultado= producto.update_producto(actz_producto)

    if not resultado:
            flash("Excelente, esta actualizado!", "success")
            return redirect("/Productos")

    flash("Error al actualizar", "error")
    return redirect("/Productos")







@app.route("/eliminar/producto/<id>", methods=['GET', 'POST'])
def delete1(id):
    if 'usuario' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/')
    
    data= {
        'id': id
    }

    producto.delete(data)
    flash("producto  eliminado", "success")
    return redirect("/Productos")