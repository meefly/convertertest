import mysql.connector
import pymongo


dbku = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = 'abcdefgh',
    database = 'mongodb'
)
x = pymongo.MongoClient('mongodb://localhost:27017')

kursor = dbku.cursor()

db = x['fantastic4']
col = db['daftarAnggota']

anggota = list(col.find())

for item in range(len(anggota)):
    newdata = anggota[item].pop('_id')

newdata2 = []
for item2 in anggota:
    newdata2.append(tuple(item2.values()))

querydb = ''' insert into daftarAnggota (nama) values (%s)'''
kursor.executemany(querydb,newdata2)
dbku.commit()