from pymongo import MongoClient
import logging as log

client = MongoClient('mongodb://localhost:27017/')

with client:

    db = client.mydatabase

    cars = db.cars.find()


    for car in cars:
        print('{0} {1}'.format(car['name'], 
            car['price']))

