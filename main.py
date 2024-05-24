from flask import Flask, jsonify, request, render_template, session, redirect, url_for
from NoSQL import NoSQL

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/table', methods=["GET"])
def routeToTable():
    opt = request.args.get("tabla")
    return render_template(f'./db/{opt}.html')

@app.route('/cliente', methods=["POST"])
def actionsCliente():
    id = int(request.form['id'])
    nombre = request.form['nombre']
    mail = request.form['mail']
    telefono = int(request.form['telefono'])
    opc = request.form['opc']

    db = NoSQL()
    msg = ""

    if opc == "Create":
        ans = db.createCliente(id, nombre, mail, telefono)
        if ans:
            msg = "Se creó el dato"
        else:
            msg = "No se pudo crear el dato. Llamar admin."
    elif opc == "Delete":
        ans = db.deleteCliente()
        if ans:
            msg = "Se eliminó el dato"
        else:
            msg = "No se pudo eliminar el dato. Llamar admin."
    elif opc == "Update":
        ans = db.updateCliente(id, nombre, mail, telefono)
        if ans:
            msg = "Se actualizó el dato"
        else:
            msg = "No se pudo actualizar el dato. Llamar admin."
    elif opc == "Retrieve":
        ans = db.retrieveCliente()
        if ans:
            msg = "" #Tabla con información
        else:
            msg = "No se encontró el dato."
    
    db.closeConn()
    return render_template("index.html")

@app.route('/restaurante', methods=["POST"])
def actionsRestaurante():
    nit = int(request.form['nit'])
    nombre = request.form['nombre']
    apertura = request.form['apertura']
    cierre = request.form['cierre']
    ubicacion = request.form['ubicacion']
    opc = request.form['opc']

    db = NoSQL()
    msg = ""

    if opc == "Create":
        ans = db.createRestaurante(nit, nombre, apertura, cierre, ubicacion)
        if ans:
            msg = "Se creó el dato"
        else:
            msg = "No se pudo crear el dato. Llamar admin."
    elif opc == "Delete":
        ans = db.deleteRestaurante()
        if ans:
            msg = "Se eliminó el dato"
        else:
            msg = "No se pudo eliminar el dato. Llamar admin."
    elif opc == "Update":
        ans = db.updateRestaurante()
        if ans:
            msg = "Se actualizó el dato"
        else:
            msg = "No se pudo actualizar el dato. Llamar admin."
    elif opc == "Retrieve":
        ans = db.retrieveRestaurante()
        if ans:
            msg = "" #Tabla con información
        else:
            msg = "No se encontró el dato."
    
    db.closeConn()

    return render_template("index.html")

@app.route('/factura', methods=["POST"])
def actionsFactura():
    nit = int(request.form['nit'])
    id = int(request.form['id'])
    prods = int(request.form['totalProductos'])
    medioPago = request.form['medioPago']
    fechaCompra = request.form['FyH']
    opc = request.form['opc']
    currProd = "1"
    productos = []

    if opc == "Create":
        return render_template("./db/detalleFactura.html", nit=nit, id=id, prods=prods, medioPago=medioPago, fechaCompra=fechaCompra, currProd=currProd, productos=productos)
    elif opc == "Delete " or opc == "Update":
        msg = "Una factura no se puede borrar ni actualizar una vez creada."
    elif opc == "Retrieve":
        db = NoSQL()
        msg = ""

@app.route('/detalleFactura', methods=["GET", "POST"])
def detalleFactura():
    if request.method == "POST":
        prod = request.form['prod']
        cantidad = request.form['cantidad']
        currProd = int(request.form['currProd']) + 1
        productos = []
        val = request.form.getlist("productosArr")
        if len(val) > 0:
            i = 0
            while i < len(val):
                newArr = [val[i], val[i+1]]
                productos.append(newArr)
                i+=2     
        amount = [prod, cantidad]
        productos.append(amount)

    prods = int(request.form['prods'])
    id = request.form['id']
    nit = request.form['nit']
    fechaCompra = request.form['fechaCompra']
    medioPago = request.form['medioPago']
    if currProd > prods:
        
        db = NoSQL()
        ans, msg = db.createFactura(productos, id, nit, medioPago, fechaCompra, prods)
        print("msg: "+msg)
        db.closeConn()
        if ans:
            pass
        return render_template("index.html")

    return render_template('./db/detalleFactura.html', nit=nit, id=id, prods=prods,medioPago=medioPago, fechaCompra=fechaCompra, currProd=currProd, productos=productos)

@app.route("/inventario", methods=["POST"])
def actionsInventario():
    nitRest = int(request.form['nitRest'])
    codProd = request.form['codProd']
    cantidad = int(request.form['cantidad'])
    opc = request.form['opc']

    db = NoSQL()
    msg = ""

    if opc == "Create":
        ans = db.createInventario(nitRest, codProd, cantidad)
        if ans:
            msg = "Se creó el dato"
        else:
            msg = "No se pudo crear el dato. Llamar admin."
    elif opc == "Delete":
        ans = db.deleteInventario()
        if ans:
            msg = "Se eliminó el dato"
        else:
            msg = "No se pudo eliminar el dato. Llamar admin."
    elif opc == "Update":
        ans = db.updateInventario(nitRest, codProd, cantidad)
        if ans:
            msg = "Se actualizó el dato"
        else:
            msg = "No se pudo actualizar el dato. Llamar admin."
    elif opc == "Retrieve":
        ans = db.retrieveInventario()

    db.closeConn()

    return render_template("index.html")

@app.route("/producto", methods=["POST"])
def actionsProducto():
    idProd = request.form['idProd']
    nitProv = int(request.form['nitProv'])
    nombre = request.form['nombre']
    precio = int(request.form['precio'])
    categoria = request.form['categoria']
    opc = request.form['opc']

    db = NoSQL()
    msg = ""

    if opc == "Create":
        ans = db.createProducto(nitProv, nombre, precio, categoria)
        if ans:
            msg = "Se creó el dato"
        else:
            msg = "No se pudo crear el dato. Llamar admin."
    elif opc == "Delete":
        ans = db.deleteProducto()
        if ans:
            msg = "Se eliminó el dato"
        else:
            msg = "No se pudo eliminar el dato. Llamar admin."
    elif opc == "Update":
        ans = db.updateProducto(idProd, nitProv, nombre, precio, categoria)
        if ans:
            msg = "Se actualizó el dato"
        else:
            msg = "No se pudo actualizar el dato. Llamar admin."
    elif opc == "Retrieve":
        ans = db.retrieveProducto()
        if ans:
            msg = "" #Tabla con información
        else:
            msg = "No se encontró el dato."
    
    db.closeConn()

    return render_template("index.html")

@app.route("/proveedor", methods=["POST"])
def actionsProveedor():
    nitProv = int(request.form['nitProv'])
    ubicacion = request.form['ubicacion']
    telefono = int(request.form['telefono'])
    opc = request.form['opc']

    db = NoSQL()
    msg = ""

    if opc == "Create":
        ans = db.createProveedor(nitProv, ubicacion, telefono)
        if ans:
            msg = "Se creó el dato"
        else:
            msg = "No se pudo crear el dato. Llamar admin."
    elif opc == "Delete":
        ans = db.deleteProveedor()
        if ans:
            msg = "Se eliminó el dato"
        else:
            msg = "No se pudo eliminar el dato. Llamar admin."
    elif opc == "Update":
        ans = db.updateProveedor(nitProv, ubicacion, telefono)
        if ans:
            msg = "Se actualizó el dato"
        else:
            msg = "No se pudo actualizar el dato. Llamar admin."
    elif opc == "Retrieve":
        ans = db.retrieveProveedor()
        if ans:
            msg = "" #Tabla con información
        else:
            msg = "No se encontró el dato."
    
    db.closeConn()

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)