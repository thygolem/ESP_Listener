import pymongo
import datetime
import time
from  pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.esp_db
collection = db.esp_collection


# set a 5-second connection timeout
#client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
#try:
#    print(client.server_info())
#except Exception:
#    print("Unable to connect to the server.")



#users_location = {
#        "usuario": "Mike",
#        "_id": 2,
#        "cargo": "Electromecánico",
#        "tags": ["work_type_1", "work_type_2", "work_type_3"],
#        "mac": "10:00:00:00:00:01",
#        "zone" : "B/F/Z",
#        "activo": True,
#        "fecha": datetime.datetime.utcnow()
#        }


status = True
zone = "B/F/Z"
while status == True:
    user_locations = db.user_locations
    t = time.strftime('%H:%M:%S')
    segundos = int(t[6:9])
    print (segundos)
    time.sleep(1)
    if segundos % 2 == 0:
        zone = "B/Z/Y"
        user_locations = user_locations.update_one({"usuario": "Mike",}, {"$set" : {"zone": zone}})
    else:
        zone = "B/Z/X"
        user_locations = user_locations.update_one({"usuario": "Mike",}, {"$set" : {"zone": zone}})


#user_locations = db.user_locations
#user_locations = user_locations.update_one({"usuario": "Mike",}, {"$set" : {"zone": "B/F/X"}})


#user_locations = user_locations.insert_one(users_location).inserted.id
#user_locations