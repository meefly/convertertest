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
querydb = '''select * from karakter'''

kursor.execute(querydb)

row=kursor.fetchall()
head=['id','nama','usia']
with open("sql2csv.csv","w",newline='') as x:
    writer = csv.writer(x)
    writer.writerow(head)
    writer.writerows(row)