from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

class NoSQL():
    def init(self):
        load_dotenv()
        self.pwd = os.getenv('DB_PASS')
        
    def DBConn(self):
        # uri = f"mongodb+srv://mgarciac10:{self.pwd}@cluster0.oxxzmnb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        uri = f"mongodb+srv://sidarragac:{self.pwd}@cluster0.t58ekeo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        client = MongoClient(uri)
        try:
            client.admin.command('ping')
            print("DONE!")
            return client
        except Exception as e:
            print(e)