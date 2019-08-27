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
querydb = '''select * from karakter'''

kursor.execute(querydb)

row=kursor.fetchall()

newDict = []
for item in range(len(row)):
    newDict.append({'id':row[item][0],'nama':row[item][1],'usia':row[item][2]})

with open('sql2json.json', 'w') as x:
    json.dump(newDict, x)
