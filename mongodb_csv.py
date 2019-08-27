import pymongo
import csv

x = pymongo.MongoClient('mongodb://localhost:27017')

db = x['supersentai']
col = db['zeo']

zeo = list(col.find())


for item in range(len(zeo)):
    zeo[item].pop('_id')

with open("mongodb2csv.csv","w",newline='') as x:
    writer = csv.DictWriter(x, fieldnames=['gaji','name','kecamatan'])
    writer.writeheader()
    writer.writerows(zeo)