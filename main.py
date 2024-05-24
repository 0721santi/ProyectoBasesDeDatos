from flask import Flask, request, render_template
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
        msg = db.createCliente(id, nombre, mail, telefono)
    elif opc == "Delete":
        if id is None:
            msg = "Faltan datos."
        else:
            msg = db.deleteCliente(id)
    elif opc == "Update":
        if id is None:
            msg = "Faltan datos."
        else:
            msg = db.updateCliente(id, nombre, mail, telefono)
    elif opc == "Retrieve":
        if id is not None:
            result, msg = db.retrieveCliente(id)
            if result is not None:
                return render_template("./db/retrieve.html", data=result, coll="cliente")
            else:
                return render_template("index.html", msg=msg)
        msg = "Faltan datos"
    db.closeConn()
    return render_template("index.html", msg=msg)

@app.route('/restaurante', methods=["POST"])
def actionsRestaurante():
    nit = int(request.form['nit'])
    nombre = request.form['nombre']
    apertura = request.form['apertura']
    cierre = request.form['cierre']
    ubicacion = request.form['ubicacion']
    opc = request.form['opc']

    db = NoSQL()

    if opc == "Create":
        msg = db.createRestaurante(nit, nombre, apertura, cierre, ubicacion)
    elif opc == "Delete":
        if nit is None:
            msg = "Faltan datos."
        else:
            msg = db.deleteRestaurante(nit)
    elif opc == "Update":
        if nit is None:
            msg = "Faltan datos."
        else:
            msg = db.updateRestaurante(nit, nombre, apertura, cierre, ubicacion)
    elif opc == "Retrieve":
        if nit is not None:
            result, msg = db.retrieveRestaurante(nit)
            if result is not None:
                return render_template("./db/retrieve.html", data=result)
        else:
            msg = "Faltan datos"
    
    db.closeConn()

    return render_template("index.html", msg=msg)

@app.route('/factura', methods=["POST"])
def actionsFactura():
    idFactura = request.form['idFactura']
    nit = request.form['nit']
    id = request.form['id']
    prods = request.form['totalProductos']
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
        if idFactura is not None:
            result, msg = db.retrieveFactura(idFactura)
            if result is not None:
                return render_template("./db/retrieve.html", data=result)
        else:
            msg = "Faltan datos"
    return render_template("index.html", msg=msg)

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
        msg = db.createFactura(productos, id, nit, medioPago, fechaCompra, prods)
        return render_template("index.html", msg=msg)

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
        msg =  db.createInventario(nitRest, codProd, cantidad)
    elif opc == "Delete":
        if nitRest is None or codProd is None:
            msg = "Faltan datos."
        else:
            msg = db.deleteInventario(nitRest, codProd)
    elif opc == "Update":
        if nitRest is None or codProd is None:
            msg = "Faltan datos."
        else:
            msg = db.updateInventario(nitRest, codProd, cantidad)
    elif opc == "Retrieve":
        if nitRest is not None and codProd is not None:
            result, msg = db.retrieveInventario(nitRest, codProd)
            return render_template("./db/retrieve.html", data=result)
        msg = "Faltan datos"

    db.closeConn()

    return render_template("index.html", msg=msg)

@app.route("/producto", methods=["POST"])
def actionsProducto():
    idProd = request.form['idProd']
    nitProv = request.form['nitProv']
    nombre = request.form['nombre']
    precio = int(request.form['precio'])
    categoria = request.form['categoria']
    opc = request.form['opc']

    db = NoSQL()
    msg = ""

    if opc == "Create":
        msg = db.createProducto(int(nitProv), nombre, precio, categoria)
    elif opc == "Delete":
        if idProd is None:
            msg = "Faltan datos."
        else:
            msg = db.deleteProducto(idProd)
    elif opc == "Update":
        if idProd is None or nitProv is None:
            msg = "Faltan datos."
        else:
            msg = db.updateProducto(idProd, int(nitProv), nombre, precio, categoria)
    elif opc == "Retrieve":
        if idProd is not None:
            result, msg = db.retrieveProducto(idProd)
            return render_template("./db/retrieve.html", data=result)
        msg = "Faltan datos"
    
    db.closeConn()

    return render_template("index.html", msg=msg)

@app.route("/proveedor", methods=["POST"])
def actionsProveedor():
    nitProv = int(request.form['nitProv'])
    ubicacion = request.form['ubicacion']
    telefono = int(request.form['telefono'])
    opc = request.form['opc']

    db = NoSQL()
    msg = ""

    if opc == "Create":
        msg = db.createProveedor(nitProv, ubicacion, telefono)
    elif opc == "Delete":
        if nitProv is None:
            msg = "Faltan datos."
        else:
            msg = db.deleteProveedor(nitProv)
    elif opc == "Update":
        if nitProv is None:
            msg = "Faltan datos."
        else:
            msg = db.updateProveedor(nitProv, ubicacion, telefono)
    elif opc == "Retrieve":
        if nitProv is not None:
            result, msg = db.retrieveProveedor(nitProv)
            return render_template("./db/retrieve.html", data=result)
        msg = "Faltan datos"
    
    db.closeConn()

    return render_template("index.html", msg=msg)

if __name__ == "__main__":
    app.run(debug=True)