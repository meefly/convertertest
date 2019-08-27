import pymongo
import json
x = pymongo.MongoClient('mongodb://localhost:27017')


NEWdoraemon = x['NEWdoraemon']
NEWtokoh = NEWdoraemon['NEWtokoh']

with open('sql2json.json') as x:
    data = json.load(x)

newdata=[]
for item in data:
    newdata.append(item)

for item2 in newdata:
    NEWtokoh.insert_one(item2)
