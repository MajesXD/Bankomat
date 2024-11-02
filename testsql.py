import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)

cursor = mydb.cursor()
cursor.execute("SELECT age FROM users where name='michal'")
age_of_michal = cursor.fetchone()[0]

print(age_of_michal)
