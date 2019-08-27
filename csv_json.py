import json
import csv

newData=[]
with open('baru.csv', 'r', newline='') as x:
    reader = csv.DictReader(x)
    for i in reader:
        newData.append(dict(i))

with open('x.json', 'w') as x:
    json.dump(newData, x)