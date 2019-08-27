import pymongo
import json

x = pymongo.MongoClient('mongodb://localhost:27017')

db = x['marvel']
col = db['avengers']

avengers = list(col.find())


for item in range(len(avengers)):
    avengers[item].pop('_id')

with open('mongodb2json.json', 'w') as x:
    json.dump(avengers, x)
