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
            return "Se ha creado el cliente"
        except Exception as e:
            return str(e)

    def createRestaurante(self, nit, nombre, apertura, cierre, ubicacion):
        colection = self.db.restaurante
        ubicacion = ubicacion.lower() 
        ubicacion = ubicacion.capitalize()
        if ubicacion != "Cafeteria principal" and ubicacion != "Cafeteria norte":
            return "La ubicacion del restaurante es inválida"
        doc = {"nitRestaurante": nit, "nombreRestaurante": nombre, "ubicacionRestaurante": ubicacion, "horaApertura": apertura, "horaCierre": cierre}
        try:
            colection.insert_one(doc)
            return "Se ha creado el restaurante"
        except Exception as e:
            return str(e)

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

                idFactura = str(factura.insert_one(doc).inserted_id)

                #Añadir detalle Factura
                for info in productos:
                    producto = info[0]
                    cantidad = info[1]
                    doc = {"factura_idFactura": idFactura, "inventario_producto_codigoProducto": producto, "cantidadComprada": int(cantidad), "inventario_restaurante_nitRestaurante": int(nit)}
                    detalleFactura.insert_one(doc)
                
                transaccion.commit_transaction()
                return "Se ha agregado la factura"
            except Exception as e :
                transaccion.abort_transaction()
                return str(e)

    def createInventario(self, nitRest, codProd, cantidad):
        try:
            colection = self.db.inventario
            objId = ObjectId(codProd)
            producto = self.db.producto.find_one({"_id": objId})
            restaurante = self.db.restaurante.find_one({"nitRestaurante": nitRest})
            if producto is None:
                raise Exception(f"No existe el producto {codProd}")
            if restaurante is None:
                raise Exception(f"No existe el restaurante {nitRest}")
            doc = {"restaurante_nitRestaurante": nitRest, "producto_codigoProducto": codProd, "cantidadDisponible":     cantidad}

            colection.insert_one(doc)
            return "Se ha agregado el inventario"
        except Exception as e:
            return str(e)

    def createProducto(self, nitProv, nombre, precio, categoria):
        colection = self.db.producto
        doc = {"nombreProducto": nombre, "precio": precio, "categoria": categoria, "proveedor_nitProveedor": nitProv}
        try:
            colection.insert_one(doc)
            return "Se ha creado el producto"
        except Exception as e:
            return str(e)

    def createProveedor(self, nitProv, ubicacion, telefono):
        colection = self.db.proveedor
        doc = {"nitProveedor": nitProv, "ubicacionProveedor": ubicacion, "telefonoProveedor": telefono}
        try:
            colection.insert_one(doc)
            return "Se ha creado el proveedor"
        except Exception as e:
            return str(e)

    def updateCliente(self, id, nombre, mail, telefono):
        colection = self.db.cliente
        pk = {'idCliente': id}
        if len(nombre) > 0:
            change = {'$set': {'nombreCliente': nombre}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
                return str(e)
        if len(mail) > 0:
            change = {'$set': {'correoCliente': mail}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
                return str(e)
        if len(str(telefono)) > 1:
            change = {'$set': {'telefonoCliente': telefono}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
                return str(e)
        return f"El cliente con id {id} ha sido actualizado"

    def updateRestaurante(self, nit, nombre, apertura, cierre, ubicacion):
        colection = self.db.restaurante
        pk = {'nitRestaurante': nit}
        if len(nombre) > 0:
            change = {'$set': {'nombreRestaurante': nombre}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
                return str(e)
        if len(str(apertura)) > 0:
            change = {'$set': {'horaApertura': apertura}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
                return str(e)
        if len(str(cierre)) > 0:
            change = {'$set': {'horaCierre': cierre}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
                return str(e)
        if len(ubicacion) > 0:
            ubicacion = ubicacion.lower() 
            ubicacion = ubicacion.capitalize()
            if ubicacion != "Cafeteria principal" and ubicacion != "Cafeteria norte":
                return "La ubicacion del restaurante es inválida"
            change = {'$set': {'ubicacionRestaurante': ubicacion}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
               return str(e)
        return f"Se ha actualizado el restaurante con NIT {nit}"

    def updateInventario(self, nitRest, codProd, cantidad):
        colection = self.db.inventario
        pk = {"$and": [{'restaurante_nitRestaurante': nitRest}, {'producto_codigoProducto': codProd}]}
        if len(str(cantidad)) > 0:
            change = {'$set': {'cantidadDisponible': cantidad}}
            try:
                colection.update_one(filter=pk, update=change)
                return "Se ha actualizado el inventario"
            except Exception as e:
                return str(e)

    def updateProducto(self, idProd, nitProv, nombre, precio, categoria):
        colection = self.db.producto
        objID = ObjectId(idProd)
        pk = {"$and": [{'_id': objID}, {'proveedor_nitProveedor': nitProv}]}
        if precio > 0:
            change = {'$set': {'precio': precio}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
                return str(e)
        if len(nombre) > 0:
            change = {'$set': {'nombreProducto': nombre}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
                return str(e)
        if len(categoria) > 0:
            change = {'$set': {'categoria': categoria}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
                return str(e)
        return f"El producto ha sido actualizado"

    def updateProveedor(self, nitProv, ubicacion, telefono):
        colection = self.db.proveedor
        pk = {'nitProveedor': nitProv}
        if len(ubicacion) > 0:
            change = {'$set': {'ubicacionProveedor': ubicacion}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
                return str(e)
        if len(str(telefono)) > 0:
            change = {'$set': {'telefono': telefono}}
            try:
                colection.update_one(filter=pk, update=change)
            except Exception as e:
                return str(e)
        return f"El proveedor con NIT {nitProv} ha sido actualizado"

    def retrieveCliente(self, id):
        try:
            colection = self.db.cliente
            data = colection.find_one({"idCliente": id})
            if data is None:
                raise Exception(f"No existe un cliente con id {id}")
            
            return data, ""
        except Exception as e:
            return None, str(e)

    def retrieveRestaurante(self, nit):
        try:
            colection = self.db.restaurante
            data = colection.find_one({"nitRestaurante": nit})
            if data is None:
                raise Exception(f"No existe un restaurante con nit {nit}")
            
            return data, ""
        except Exception as e:
            return None, str(e)

    def retrieveFactura(self, idFactura):
        try:
            factura = self.db.factura
            detalleFactura = self.db.detallefactura
            objId = ObjectId(idFactura)
            infoFactura = factura.find_one({"_id": objId})
            if infoFactura is None:
                raise Exception(f"No existe una factura con id {idFactura}")
            
            detallesFactura = detalleFactura.find({"factura_idFactura": idFactura})
            i = 1
            for detalle in detallesFactura:
                for key in detalle:
                    value = detalle[key]
                    infoFactura[key+f" Producto {i}:"] = value
                i+=1
            return infoFactura, ""
        except Exception as e:
            return None, str(e)
    
    def retrieveInventario(self, nit, codProd):
        try:
            colection = self.db.inventario
            data = colection.find_one({"$and": [{'restaurante_nitRestaurante': nit}, {'producto_codigoProducto': codProd}]})
            if data is None:
                raise Exception(f"No existe un cliente con id {id}")
            
            return data, ""
        except Exception as e:
            return None, str(e)

    def retrieveProducto(self, codProd):
        try:
            colection = self.db.producto
            objId = ObjectId(codProd)
            data = colection.find_one({"_id": objId})
            if data is None:
                raise Exception(f"No existe un cliente con id {id}")
            
            return data, ""
        except Exception as e:
            return None, str(e)

    def retrieveProveedor(self, nit):
        try:
            colection = self.db.proveedor
            data = colection.find_one({"nitProveedor": nit})
            if data is None:
                raise Exception(f"No existe un cliente con id {id}")
            return data, ""
        except Exception as e:
            return None, str(e)

    def deleteCliente(self, id):
        try:
            colection = self.db.cliente
            num = colection.delete_one({"idCliente": id}).deleted_count
            if num == 0:
                raise Exception(f"No existe un cliente con id {id}")
            
            return "Se ha eliminado exitosamente"
        except Exception as e:
            return str(e)

    def deleteRestaurante(self, nit):
        try:
            colection = self.db.restaurante
            num = colection.delete_one({"nitRestaurante": nit}).deleted_count
            if num == 0:
                raise Exception(f"No existe un restaurante con nit {nit}")
            
            return "Se ha eliminado exitosamente"
        except Exception as e:
            return str(e)

    def deleteInventario(self, nit, codProd):
        try:
            colection = self.db.inventario
            num = colection.delete_one({"$and": [{'restaurante_nitRestaurante': nit}, {'producto_codigoProducto': codProd}]}).deleted_count
            if num == 0:
                raise Exception(f"No existe un ningún inventario con los datos proveeidos")
            
            return "Se ha eliminado exitosamente"
        except Exception as e:
            return str(e)

    def deleteProducto(self, codProd):
        try:
            colection = self.db.producto
            objId = ObjectId(codProd)
            num = colection.delete_one({"_id": objId}).deleted_count
            if num == 0:
                raise Exception(f"No existe un cliente con id {id}")
            
            return "Se ha eliminado exitosamente"
        except Exception as e:
            return str(e)

    def deleteProveedor(self, nit):
        try:
            colection = self.db.proveedor
            num = colection.delete_one({"nitProveedor": nit}).deleted_count
            if num == 0:
                raise Exception(f"No existe un proveedor con nit {nit}")
            
            return "Se ha eliminado exitosamente"
        except Exception as e:
            return str(e)