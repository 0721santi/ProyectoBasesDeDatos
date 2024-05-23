from pymongo.mongo_client import MongoClient
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

    def createFactura(self):
        pass

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

    def updateProducto(self, nitProv, nombre, precio, categoria):
        pass

    def updateProveedor(self):
        pass

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