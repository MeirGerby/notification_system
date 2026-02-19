from pymongo import MongoClient

MONGO_INITDB_DATABASE: str =  'data'
COLLECTION_NAME: str = 'notification' 

# MONGO_URL = "mongodb://mongo:27017"
MONGO_URL: str = "mongodb://localhost:27017/"
class MongoDB():
    _instance = None
    _connection = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MongoDB, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    @staticmethod    
    def _get_connection():
        if MongoDB._connection is None:
            MongoDB._connection = MongoClient(MONGO_URL)
            print('Connected to MongoDB...')
        return MongoDB._connection

    @staticmethod
    def _db(client):
        db = client[MONGO_INITDB_DATABASE]
        return db 
    
    @staticmethod
    def get_collection(collection_name):
        conn = MongoDB._get_connection()
        db = MongoDB._db(conn)
        coll = db[collection_name]
        return coll
