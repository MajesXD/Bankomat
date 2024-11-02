import mysql.connector

connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="bank"
)

cursor = connection.cursor()
print('Witaj w bankomacie\n')

try:
    input_numer_karty = str(input('Podaj swój numer karty\n'))
    # input_pin = input('Podaj kod pin')
    sql = "SELECT pin FROM users where numer_karty = %s"
    cursor.execute(sql, (input_numer_karty,))
    user_pin = cursor.fetchone()[0]
    print(user_pin)
except:
    print('Nieprawidłowy numer karty\n')

login_pin = int(input('Podaj numer PIN\n'))
if login_pin != user_pin:
    sql = "UPDATE users SET ban=TRUE WHERE numer_karty=%s"
    cursor.execute(sql, (input_numer_karty,))
    connection.commit()
    print("Nieprawidłowy kod PIN\n Twoje konto zostało zablokowane na godzinę")
else:
    print('ok')




