import pymongo
import csv
x = pymongo.MongoClient('mongodb://localhost:27017')

doraemon = x['doraemon']
tokoh = doraemon['tokoh']

newData=[]
with open('sql2csv.csv', 'r', newline='') as x:
    reader = csv.DictReader(x)
    for i in reader:
        newData.append(dict(i))

for item in newData:
    tokoh.insert_one(item)

