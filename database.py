import mysql.connector

database=  mysql.connector.connect(
  host="localhost",
  user="root",
  password="webcreationz@1234",
  database="db1"
)
cur = database.cursor()
n = "SELECT * FROM bmiheight"

cur.execute(n) # for single execcute  and for multiple rows use executemany
result = cur.fetchall()
for rec in result:
    print(rec)

