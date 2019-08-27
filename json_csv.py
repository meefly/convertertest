import json
import csv


with open('data.json') as x:
    data = json.load(x)

with open('baru.csv', 'w', newline='') as x:
    writer = csv.DictWriter(x, fieldnames=['nama','usia'])
    writer.writeheader()
    writer.writerows(data)
