# tutorial de FAZTWEB https://www.youtube.com/watch?v=NVoeBH0uBHo

from pymongo import MongoClient
import time
MONGO_URI = 'mongodb://localhost'

MongoClient(MONGO_URI)

client = MongoClient(MONGO_URI)

db = client['ESP32DB']
collection = db['MAC']


number_of_items = collection.count_documents({})
print(number_of_items)

# test 12
#collection.update_one({"name" : "laptop"}, {"$inc" : {"price":30}})


# test 11 incrementar un valor
#collection.update_one({"name" : "phone"}, {"$inc" : {"price":30}})


# test 10 actualizar un dato, $set=establecer los nuevos datos, los datos que queremos reemplazar
#collection.update_one({"name": "mouse"}, {"$set": {"name": "phone", "price": 600}})

#test 9 insertar 
collection.insert_one({"name":"laptop"})
#collection.update_one({"name": "laptop"}, {"$set": {"name": "phone", "price": 500}})

# test 8 eliminar todos los objetos
#collection.delete_many({})


# test 7 eliminar un objeto
#collection.delete_one({"price": 300})

# test 6 eliminar varios objetos con filtrado (criterio)
#collection.delete_many({"name": "mouse"})


#test 5 consultar un dato dentro de un objeto de una colleción
#result = collection.find_one({"name": "keyboard"})
#print(result['price'])


#test 4 consultar y filtrar un dato dentro de un objeto dentro de una colleción
#results = collection.find({"price":300})
#for eachResult in results:
#    print (eachResult['name'])



# test3 consultar objetos dentro de collección
#results = collection.find()
#for eachResult in results:
#    print (eachResult['name'])
#    time.sleep(1)
#    print (eachResult['price'])
#    time.sleep(1)
#    print (eachResult)


#test2: Insertar varios objetos en una colleccion
#product_one = {"name": "mouse"}
#product_two = {"name": "monitor"}
#collection.insert_many([product_one, product_two])

#test1: nuevo objeto dentro de una collección
# por defecto MongoDb nos da un _id, pero podemos dárselo nosotrxs también
#collection.insert_one({"_id": 0, "name": "keyboard", "price": 300})