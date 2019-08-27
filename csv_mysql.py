import csv
import mysql.connector

dbku = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = 'abcdefgh',
    database = 'doraemon'
)

kursor = dbku.cursor()

newData=[]
with open('sql2csv.csv', 'r', newline='') as x:
    reader = csv.reader(x)
    for i in reader:
        newData.append(tuple(i))

print(newData)

# querydb = ''' insert into karakter2(id,nama,usia) values (%s,%s,%s)'''
# kursor.executemany(querydb,newData[1:])
# dbku.commit()

