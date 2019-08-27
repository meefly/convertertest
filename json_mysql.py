import json
import mysql.connector

dbku = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = 'abcdefgh',
    database = 'doraemon'
)

kursor = dbku.cursor()

with open('sql2json.json') as x:
    data = json.load(x)
    
newdata=[]
newdata2=[]
for item in range(len(data)):
    for item2 in data[item].keys():
        newdata.append(data[item][item2])
    newdata2.append(tuple(newdata))

querydb = ''' insert into karakter3 (id,nama,usia) values (%s,%s,%s)'''
kursor.executemany(querydb,newdata2)
dbku.commit()