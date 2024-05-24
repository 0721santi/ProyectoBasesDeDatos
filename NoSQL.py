from pymongo.mongo_client import MongoClient
from pymongo.bulk import ObjectId
from dotenv import load_dotenv
import os

class NoSQL():
    def __init__(self):
        load_dotenv()
        pwd = os.getenv('DB_PASS')
        uri = f"mongodb+srv://mgarciac10:{pwd}@cluster0.oxxzmnb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        self.client = MongoClient(uri)
        try:
            self.client.admin.command('ping')
            self.db = self.client.proyectobd
        except Exception as e:
            print(f'Exception: {e}')
    
    def closeConn(self):
        self.client.close()

    def createCliente(self, id, nombre, mail, telefono):
        colection = self.db.cliente
        doc = {"idCliente": id, "nombreCliente": nombre, "correoCliente": mail, "telefonoCliente": telefono}
        try:
            colection.insert_one(doc)
            return True
        except Exception as e:
            print(e)
            return False

    def createRestaurante(self, nit, nombre, apertura, cierre, ubicacion):
        colection = self.db.restaurante
        doc = {"nitRestaurante": nit, "nombreRestaurante": nombre, "ubicacionRestaurante": ubicacion, "horaApertura": apertura, "horaCierre": cierre}
        try:
            colection.insert_one(doc)
            return True
        except Exception as e:
            print(e)
            return False

    def createFactura(self, productos, id, nit, medioPago, fechaCompra, totalProductos):
        with self.client.start_session() as transaccion:
            try:
                transaccion.start_transaction()
                factura = self.db.factura
                detalleFactura = self.db.detallefactura
                collProducto = self.db.producto
                #Revisa que si existen cliente y restaurante
                cliente = self.db.cliente.find_one({"idCliente": int(id)})
                restaurante = self.db.restaurante.find_one({"nitRestaurante": int(nit)})
    
                if cliente is None:
                    raise Exception("No existe ese cliente")
                if restaurante is None:
                    raise Exception("No existe ese restaurante")
    
                #Inicia transacción
                valorTotal = 0
                for info in productos:
                    producto = info[0]
                    cantidad = int(info[1])
                    pk = {"$and": [{'producto_codigoProducto': producto}, {'restaurante_nitRestaurante': int(nit)}]}
                    disponible = self.db.inventario.find_one(pk)['cantidadDisponible']
                    if int(cantidad) > disponible:
                        raise Exception(f"No hay suficientes productos de {producto}")
                    else:
                        objId = ObjectId(producto)
                        valorTotal += collProducto.find_one({'_id': objId})['precio']
                        self.updateInventario(nit, producto, (disponible-cantidad))

                #Añadir factura
                detallePago = {"totalValor": valorTotal, "medioDePago": medioPago}

                doc = {"cliente_idCliente": int(id), "restaurante_nitRestaurante": int(nit), "detallePago": detallePago, "fechaYHora": fechaCompra, "totalProductos": int(totalProductos)}

                idFactura = factura.insert_one(doc).inserted_id

                #Añandir detalle Factura
                for info in productos:
                    producto = info[0]
                    cantidad = info[1]
                    doc = {"factura_idFactura": idFactura, "inventario_producto_codigoProducto": producto, "cantidadComprada": int(cantidad), "inventario_restaurante_nitRestaurante": int(nit)}
                    detalleFactura.insert_one(doc)
                
                transaccion.commit_transaction()
                return True, "Se ha agregado la factura"
            except Exception as e :
                transaccion.abort_transaction()
                return False, str(e)

    def createInventario(self, nitRest, codProd, cantidad):
        colection = self.db.inventario
        doc = {"restaurante_nitRestaurante": nitRest, "producto_codigoProducto": codProd, "cantidadDisponible": cantidad}
        try:
            colection.insert_one(doc)
            return True
        except Exception as e:
            print(e)
            return False

    def createProducto(self, nitProv, nombre, precio, categoria):
        colection = self.db.producto
        doc = {"nombreProducto": nombre, "precio": precio, "categoria": categoria, "proveedor_nitProveedor": nitProv}
        try:
            colection.insert_one(doc)
            return True
        except Exception as e:
            print(e)
            return False

    def createProveedor(self, nitProv, ubicacion, telefono):
        colection = self.db.proveedor
        doc = {"nitProveedor": nitProv, "ubicacionProveedor": ubicacion, "telefonoProveedor": telefono}
        try:
            colection.insert_one(doc)
            return True
        except Exception as e:
            print(e)
            return False

    def updateCliente(self, id, nombre, mail, telefono):
        colection = self.db.cliente
        pk = {'idCliente': id}
        if len(nombre) > 0:
            change = {'$set': {'nombreCliente': nombre}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
                print(e)
                return False
        if len(mail) > 0:
            change = {'$set': {'correoCliente': mail}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
                print(e)
                return False
        if len(str(telefono)) > 1:
            change = {'$set': {'telefonoCliente': telefono}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
                print(e)
        return True

    def updateRestaurante(self, nit, nombre, apertura, cierre, ubicacion):
        colection = self.db.restaurante
        pk = {'nitRestaurante': nit}
        if len(nombre) > 0:
            change = {'$set': {'nombreRestaurante': nombre}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
                print(e)
                return False
        if len(str(apertura)) > 0:
            change = {'$set': {'horaApertura': apertura}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
                print(e)
                return False
        if len(str(cierre)) > 0:
            change = {'$set': {'horaCierre': cierre}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
                print(e)
        if len(ubicacion) > 0:
            change = {'$set': {'ubicacionRestaurante': ubicacion}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
                print(e)
        return True

    def updateInventario(self, nitRest, codProd, cantidad):
        colection = self.db.inventario
        pk = {"$and": [{'restaurante_nitRestaurante': nitRest}, {'producto_codigoProducto': codProd}]}
        if len(str(cantidad)) > 0:
            change = {'$set': {'cantidadDisponible': cantidad}}
            try:
                colection.update_one(filter=pk, update=change)
                return True
            except Exception as e:
                print(e)
                return False

    def updateProducto(self, idProd, nitProv, nombre, precio, categoria):
        colection = self.db.producto
        objID = ObjectId(idProd)
        print(objID)
        pk = {"$and": [{'_id': objID}, {'proveedor_nitProveedor': nitProv}]}
        if precio > 0:
            change = {'$set': {'precio': precio}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
                print(e)
                return False
        if len(nombre) > 0:
            change = {'$set': {'nombreProducto': nombre}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
                print(e)
        if len(categoria) > 0:
            change = {'$set': {'categoria': categoria}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
                print(e)
        return True

    def updateProveedor(self, nitProv, ubicacion, telefono):
        colection = self.db.proveedor
        pk = {'nitProveedor': nitProv}
        if len(ubicacion) > 0:
            change = {'$set': {'ubicacionProveedor': ubicacion}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
                print(e)
                return False
        if len(str(telefono)) > 0:
            change = {'$set': {'telefono': telefono}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
                print(e)
                return False
        return True

    def retrieveCliente(self):
        pass

    def retrieveRestaurante(self):
        pass

    def retrieveFactura(self):
        pass
    
    def retrieveInventario(self):
        pass

    def retrieveProducto(self):
        pass

    def retrieveProveedor(self):
        pass

    def deleteCliente(self):
        pass

    def deleteRestaurante(self):
        pass

    def deleteInventario(self):
        pass

    def deleteProducto(self):
        pass

    def deleteProveedor(self):
        pass