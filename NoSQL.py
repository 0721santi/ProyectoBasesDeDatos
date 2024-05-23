from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

class NoSQL():
    def __init__(self):
        load_dotenv()
        pwd = os.getenv('DB_PASS')
        uri = f"mongodb+srv://sidarragac:{pwd}@cluster0.t58ekeo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        # uri = f"mongodb+srv://mgarciac10:{pwd}@cluster0.oxxzmnb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        self.client = MongoClient(uri)
        try:
            self.client.admin.command('ping')
            self.db = self.client.sample_mflix
        except Exception as e:
            print(f'Exception: {e}')
    
    def closeConn(self):
        self.client.close()

    def createCliente(self):
        pass

    def createRestaurante(self):
        pass

    def createFactura(self):
        pass

    def createInventario(self):
        pass

    def createProducto(self):
        pass

    def createProveedor(self):
        pass

    def updateCliente(self):
        pass

    def updateRestaurante(self):
        pass

    def updateFactura(self):
        pass

    def updateInventario(self):
        pass

    def updateProducto(self):
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

    def deleteFactura(self):
        pass

    def deleteInventario(self):
        pass

    def deleteProducto(self):
        pass

    def deleteProveedor(self):
        pass