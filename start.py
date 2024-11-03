import mysql.connector
from datetime import datetime, timedelta

#Połączenie z bazą danych
connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="bank"
)
cursor = connection.cursor()

print('Witaj w bankomacie')
input_numer_karty = int(input('Podaj swój numer karty\n'))

#Sprawdzanie numeru karty
sql = "SELECT numer_karty FROM users"
cursor.execute(sql)
baza_numerow = cursor.fetchall()

if not (input_numer_karty,) in baza_numerow:
    print('Nieprawidłowy numer karty')
    exit()
else:
    #Sprawdzanie czy jest ban
    sql = "SELECT ban FROM users WHERE numer_karty = %s"
    cursor.execute(sql, (input_numer_karty,))
    unban_time = cursor.fetchone()[0]
    if unban_time > datetime.now():
        print('Twoje konto jest zablokowane do ' + unban_time.strftime("%Y-%m-%d %H:%M:%S"))
        exit()
    else:
        sql = "SELECT pin FROM users where numer_karty = %s"
        cursor.execute(sql, (input_numer_karty,))
        user_pin = cursor.fetchone()[0]

#Podanie pinu
login_pin = int(input('Podaj numer PIN\n'))

if login_pin != user_pin:
    unban_moment = datetime.now() + timedelta(hours=1)
    sql = "UPDATE users SET ban=%s WHERE numer_karty=%s"
    cursor.execute(sql, (unban_moment, input_numer_karty)) 
    connection.commit()
    print("Nieprawidłowy kod PIN\n Twoje konto zostało zablokowane do\n" + unban_moment.strftime("%Y-%m-%d %H:%M:%S"))

else:
    quota = int(input('Podaj kwotę do wypłaty\n'))
    sql = "SELECT bilans FROM users where numer_karty = %s"
    cursor.execute(sql, (input_numer_karty,))
    acc_balance = cursor.fetchone()[0]

if quota > acc_balance:
    unban_moment = datetime.now() + timedelta(days=1)
    sql = "UPDATE users SET ban=%s WHERE numer_karty=%s"
    cursor.execute(sql, (unban_moment, input_numer_karty)) 
    connection.commit()
    print('Nie posiadasz tyle pieniędzy na koncie. Twoje konto zostało zablokowane do ' + unban_moment.strftime("%Y-%m-%d %H:%M:%S"))
    exit()
else:
    def cashout ():
        print(quota)




        
    cashout()