import mysql.connector
from datetime import datetime, timedelta

#Połączenie z bazą danych////////////////////
connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="bank"
)
cursor = connection.cursor()

print('Witaj w bankomacie')
input_numer_karty = int(input('Podaj swój numer karty\n'))

#Sprawdzanie numeru karty///////////////////
sql = "SELECT numer_karty FROM users"
cursor.execute(sql)
baza_numerow = cursor.fetchall()

if not (input_numer_karty,) in baza_numerow:
    print('Nieprawidłowy numer karty')
    exit()
else:
    #Sprawdzanie czy jest ban////////////////////////////
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

#Podanie pinu///////////////////////////////////
login_pin = int(input('Podaj numer PIN\n'))

if login_pin != user_pin:
    unban_moment = datetime.now() + timedelta(hours=1)
    sql = "UPDATE users SET ban=%s WHERE numer_karty=%s"
    cursor.execute(sql, (unban_moment, input_numer_karty)) 
    connection.commit()
    print("Nieprawidłowy kod PIN\n Twoje konto zostało zablokowane do\n" + unban_moment.strftime("%Y-%m-%d %H:%M:%S"))

else:
    while True:
        quota = int(input('Podaj kwotę do wypłaty\n'))
        if quota > 500:
            print("Kwota nie może być większa niż 500")
            continue
        elif quota % 10 > 0:
            print("Kwota musi być podzielna przez 10")
            continue
        else:
            sql = "SELECT bilans FROM users where numer_karty = %s"
            cursor.execute(sql, (input_numer_karty,))
            acc_balance = cursor.fetchone()[0]
            break

if quota > acc_balance:
    unban_moment = datetime.now() + timedelta(days=1)
    sql = "UPDATE users SET ban=%s WHERE numer_karty=%s"
    cursor.execute(sql, (unban_moment, input_numer_karty)) 
    connection.commit()
    print('Nie posiadasz tyle pieniędzy na koncie. Twoje konto zostało zablokowane do ' + unban_moment.strftime("%Y-%m-%d %H:%M:%S"))
    exit()
else:

    def cashout ():
        quota_operation = int(quota)

        #SPRAWDZANIE 200------------------------------------------------------------------------------------------------------------------200
        sql = "SELECT ilosc FROM bankomat WHERE nominal = '200'"
        cursor.execute(sql)
        amount_200 = cursor.fetchone()[0]

        #Czy w kwocie mieszczą sie 200 i ile
        if quota_operation // 200 > 0:
            quantity = quota_operation // 200 
            value = quantity * 200 
        else:
            quantity = 0
            value = quota_operation

        #Jeśli w bazie jest mniej lub tyle samo banknotów
        if amount_200 <= quantity and amount_200 > 0:
            quantity = amount_200
            value = quantity * 200
            quota_operation = quota_operation - value
            take_200 = quantity
            print('do zabrania 200 ' + str(take_200))

        #Jeśli w bazie jest więcej banknotów
        elif amount_200 > quantity and amount_200 > 0:
            value = quantity * 200
            quota_operation = quota_operation - value
            take_200 = quantity
            print('do zabrania 200 ' + str(take_200))

        #Jeśli nie ma banknotów
        else:
            print('pierwsza kwota 200 ' + str(quota_operation))
            quantity = 0
            value = quota_operation
            quota_operation = quota_operation - value
            take_200 = 0
            print('po odjeciu value 200 ' + str(quota_operation))
            print("next operation 200\n")

        #SPRAWDZANIE 100------------------------------------------------------------------------------------------------------------------100
        sql = "SELECT ilosc FROM bankomat WHERE nominal = '100'"
        cursor.execute(sql)
        amount_100 = cursor.fetchone()[0]

        #Czy w kwocie mieszczą sie 100 i ile
        if quota_operation // 100 > 0:
            quantity = quota_operation // 100 
            value = quantity * 100 
        else:
            quantity = 0
            value = quota_operation

        #Jeśli w bazie jest mniej lub tyle samo banknotów
        if amount_100 <= quantity and amount_100 > 0:
            quantity = amount_100
            value = quantity * 100
            quota_operation = quota_operation - value
            take_100 = quantity
            print('do zabrania 100 ' + str(take_100))

        #Jeśli w bazie jest więcej banknotów
        elif amount_100 > quantity and amount_100 > 0:
            value = quantity * 100
            quota_operation = quota_operation - value
            take_100 = quantity
            print('do zabrania 100 ' + str(take_100))
        #Jeśli nie ma banknotów
        else:
            print('pierwsza kwota 100 ' + str(quota_operation))
            quantity = 0
            value = quota_operation
            quota_operation = quota_operation - value
            take_100 = 0
            print('po odjeciu value 100 ' + str(quota_operation))
            print("next operation 100\n")

        #SPRAWDZANIE 50-------------------------------------------------------------------------------------------------------------------50
        sql = "SELECT ilosc FROM bankomat WHERE nominal = '50'"
        cursor.execute(sql)
        amount_50 = cursor.fetchone()[0]

        #Czy w kwocie mieszczą sie 50 i ile
        if quota_operation // 50 > 0:
            quantity = quota_operation // 50 
            value = quantity * 50 
        else:
            quantity = 0
            value = quota_operation

        #Jeśli w bazie jest mniej lub tyle samo banknotów
        if amount_50 <= quantity and amount_50 > 0:
            quantity = amount_50
            value = quantity * 50
            quota_operation = quota_operation - value
            take_50 = quantity
            print('do zabrania 50 ' + str(take_50))
            
        #Jeśli w bazie jest więcej banknotów
        elif amount_50 > quantity and amount_50 > 0:
            value = quantity * 50
            quota_operation = quota_operation - value
            take_50 = quantity
            print('do zabrania 50 ' + str(take_50))
        #Jeśli nie ma banknotów
        else:
            print('pierwsza kwota 50 ' + str(quota_operation))
            quantity = 0
            value = quota_operation
            quota_operation = quota_operation - value
            take_50 = 0
            print('po odjeciu value 50 ' + str(quota_operation))
            print("next operation 50\n")    

        #SPRAWDZANIE 20-------------------------------------------------------------------------------------------------------------------20
        sql = "SELECT ilosc FROM bankomat WHERE nominal = '20'"
        cursor.execute(sql)
        amount_20 = cursor.fetchone()[0]

        #Czy w kwocie mieszczą sie 20 i ile
        if quota_operation // 20 > 0:
            quantity = quota_operation // 20 
            value = quantity * 20 
        else:
            quantity = 0
            value = quota_operation

        #Jeśli w bazie jest mniej lub tyle samo banknotów
        if amount_20 <= quantity and amount_20 > 0:
            quantity = amount_20
            value = quantity * 20
            quota_operation = quota_operation - value
            take_20 = quantity
            print('do zabrania 20 ' + str(take_20))
            
        #Jeśli w bazie jest więcej banknotów
        elif amount_20 > quantity and amount_20 > 0:
            value = quantity * 20
            quota_operation = quota_operation - value
            take_20 = quantity
            print('do zabrania 20 ' + str(take_20))
        #Jeśli nie ma banknotów
        else:
            print('pierwsza kwota 20 ' + str(quota_operation))
            quantity = 0
            value = quota_operation
            quota_operation = quota_operation - value
            take_20 = 0
            print('po odjeciu value 20 ' + str(quota_operation))
            print("next operation 20\n")

        #SPRAWDZANIE 10-------------------------------------------------------------------------------------------------------------------10
        sql = "SELECT ilosc FROM bankomat WHERE nominal = '10'"
        cursor.execute(sql)
        amount_10 = cursor.fetchone()[0]

        #Czy w kwocie mieszczą sie 10 i ile
        if quota_operation // 10 > 0:
            quantity = quota_operation // 10 
            value = quantity * 10 
        else:
            quantity = 0
            value = quota_operation

        #Jeśli w bazie jest mniej lub tyle samo banknotów
        if amount_10 <= quantity and amount_10 > 0:
            quantity = amount_10
            value = quantity * 10
            quota_operation = quota_operation - value
            take_10 = quantity
            print('do zabrania 10' + str(take_10))
            
        #Jeśli w bazie jest więcej banknotów
        elif amount_10 > quantity and amount_10 > 0:
            value = quantity * 10
            quota_operation = quota_operation - value
            take_10 = quantity
            print('do zabrania 10 ' + str(take_10))
        #Jeśli nie ma banknotów
        else:
            print('pierwsza kwota 10 ' + str(quota_operation))
            quantity = 0
            value = quota_operation
            quota_operation = quota_operation - value
            take_10 = 0
            print('po odjeciu value 10 ' + str(quota_operation))
            print("next operation 10\n")
        #Koniec---------------------------------------------------------------------------------------------------------------------------

        #Update do bazy bankomat
        new_amount_200 = amount_200 - take_200
        sql = "UPDATE bankomat SET ilosc = %s WHERE nominal='200'"
        cursor.execute(sql, (new_amount_200,))
        connection.commit()

        sql = "UPDATE bankomat SET ilosc = %s WHERE nominal='100'"
        new_amount_100 = amount_100 - take_100
        cursor.execute(sql, (new_amount_100,))
        connection.commit()

        sql = "UPDATE bankomat SET ilosc = %s WHERE nominal='50'"
        new_amount_50 = amount_50 - take_50
        cursor.execute(sql, (new_amount_50,))
        connection.commit()

        sql = "UPDATE bankomat SET ilosc = %s WHERE nominal='20'"
        new_amount_20 = amount_20 - take_20
        cursor.execute(sql, (new_amount_20,))
        connection.commit()

        sql = "UPDATE bankomat SET ilosc = %s WHERE nominal='10'"
        new_amount_10 = amount_10 - take_10
        cursor.execute(sql, (new_amount_10,))
        connection.commit()




        #Update do bazy users
        new_quota = acc_balance - quota
        sql = "UPDATE users SET bilans=%s WHERE numer_karty=%s"
        cursor.execute(sql, (new_quota, input_numer_karty))
        connection.commit()

    cashout()
