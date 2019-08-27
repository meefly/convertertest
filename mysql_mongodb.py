import mysql.connector
import pymongo

x = pymongo.MongoClient('mongodb://localhost:27017')
dbku = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = 'abcdefgh',
    database = 'supersentai'
)

kursor = dbku.cursor()

supersentai = x['supersentai']
zeo = supersentai['zeo']

querydb = '''select * from zeo'''
kursor.execute(querydb)
row = kursor.fetchall()

newdata = []
for item in row:
    newdata.append({'gaji':item[0],'name':item[1],'kecamatan':item[2]})

for item2 in newdata:
    zeo.insert_one(item2)