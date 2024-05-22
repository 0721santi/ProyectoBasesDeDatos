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