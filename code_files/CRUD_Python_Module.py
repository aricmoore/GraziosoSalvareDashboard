from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson.objectid import ObjectId 

class AnimalShelter(object):

    def __init__(self, username, password,
                 host="localhost", port=27017, db_name="aac", collection="animals"):

        # Stores params
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.db_name = db_name
        self.collection_name = collection

        # Builds URI
        uri = f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}/?authSource=admin"

        try:
            self.client = MongoClient(uri)
        except Exception as e:
            print("Error: Unable to connect to MongoDB:", e)
            raise e

        self.database = self.client[self.db_name]
        self.collection = self.database[self.collection_name]


    # Helper method to return the next available record number for use in the create method
    def get_next_animal_id(self):
        try:
            # Finds the last inserted document sorted by animal_id descending
            last_doc = self.collection.find_one(sort=[("animal_id", -1)])
            if last_doc and "animal_id" in last_doc:
                last_id = last_doc["animal_id"]
                # We're assuming animal_id is something like "A12345"
                numeric_part = int(last_id[1:])  # removes letter and convert to int
                return f"A{numeric_part + 1}"    # increments and return as string
            else:
                return "A1"                      # starts numbering if collection is empty
        except Exception as e:
            print(f"Failed to get next animal_id: {e}")
            return "A1"
    
    # ************** CREATE **************
    def create(self, data):
        # Exits early if condition is met, pseudo short-circuit
        if data is None:
            raise Exception("Nothing to save, because data parameter is empty")

        try:
            # Auto-assigns animal_id if caller did not provide it
            if "animal_id" not in data:
                data["animal_id"] = self.get_next_animal_id()

            # Prevents duplicate animal_id
            if self.collection.count_documents({"animal_id": data["animal_id"]}, limit=1):
                print(f"Insert failed: animal_id {data['animal_id']} already exists.")
                return False

            result = self.collection.insert_one(data)
            return True if result.acknowledged else False

        except Exception as e:
            print(f"Insert failed: {e}")
            return False

    # ************** READ **************
    def read(self, query):
        # Exits early
        if query is None:
            return []
        try:
            cursor = self.collection.find(query)  # uses find() as specified
            return list(cursor)                   # converts cursor to list
        except Exception as e:
            print(f"Query failed: {e}")
            return []
        
    # ************** UPDATE **************
    def update(self, query, new_values):
        if query is None or new_values is None:
            raise Exception("Both query and new_values parameters are required")

        try:
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        except Exception as e:
            print(f"Update failed: {e}")
            return 0
    
    # ************** DELETE **************
    def delete(self, query):
        if query is None:
            raise Exception("Query parameter is required for delete operation")

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Delete failed: {e}")
            return 0