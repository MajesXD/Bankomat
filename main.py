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
    quota_operation = int(quota)

    #Wyciąganie ilości banknotów z bazy
    sql = "SELECT ilosc FROM bankomat WHERE nominal = '200'"
    cursor.execute(sql)
    amount_200 = cursor.fetchone()[0]

    sql = "SELECT ilosc FROM bankomat WHERE nominal = '100'"
    cursor.execute(sql)
    amount_100 = cursor.fetchone()[0]

    sql = "SELECT ilosc FROM bankomat WHERE nominal = '50'"
    cursor.execute(sql)
    amount_50 = cursor.fetchone()[0]
    
    sql = "SELECT ilosc FROM bankomat WHERE nominal = '20'"
    cursor.execute(sql)
    amount_20 = cursor.fetchone()[0]

    sql = "SELECT ilosc FROM bankomat WHERE nominal = '10'"
    cursor.execute(sql)
    amount_10 = cursor.fetchone()[0]


    #SPRAWDZANIE 200------------------------------------------------------------------------------------------------------------------200
    def spr_200(quota_operation, amount_200):

        #Czy w kwocie mieszczą sie 200 i ile
        if quota_operation // 200 > 0:
            quantity = quota_operation // 200 
            value = quantity * 200 
        else:
            quantity = 0
            value = quota_operation

        #Jeśli w bazie jest więcej lub tyle samo banknotów
        if amount_200 >= quantity and amount_200 > 0:
            value = quantity * 200
            value_200 = value
            quota_operation = quota_operation - value
            take_200 = quantity
            print('do zabrania 200 ' + str(take_200))
        
        #Jeśli w bazie jest mniej banknotów
        elif amount_200 < quantity and amount_200 > 0:
            quantity = amount_200
            value = quantity * 200
            value_200 = value
            quota_operation = quota_operation - value
            take_200 = quantity
            
            print('do zabrania 200 ' + str(take_200))

        #Jeśli nie ma banknotów
        else:
            print('pierwsza kwota 200 ' + str(quota_operation))
            quantity = 0
            value = 0
            value_200 = value
            quota_operation = quota_operation - value
            take_200 = 0
            print('po odjeciu value 200 ' + str(quota_operation))
            print("next operation 200\n")
        return value, quota_operation, take_200, value_200
    
    #SPRAWDZANIE 100------------------------------------------------------------------------------------------------------------------100
    def spr_100(quota_operation, amount_100):

        #Czy w kwocie mieszczą sie 100 i ile
        if quota_operation // 100 > 0:
            quantity = quota_operation // 100 
            value = quantity * 100 
        else:
            quantity = 0
            value = quota_operation

        #Jeśli w bazie jest więcej lub tyle samo banknotów
        if amount_100 >= quantity and amount_100 > 0:
            value = quantity * 100
            value_100 = value
            quota_operation = quota_operation - value
            take_100 = quantity
            print('do zabrania 100 ' + str(take_100))

        #Jeśli w bazie jest mniej banknotów
        elif amount_100 < quantity and amount_100 > 0:
            quantity = amount_100
            value = quantity * 100
            value_100 = value
            quota_operation = quota_operation - value
            take_100 = quantity
            print('do zabrania 100 ' + str(take_100))

        #Jeśli nie ma banknotów
        else:
            print('pierwsza kwota 100 ' + str(quota_operation))
            quantity = 0
            value = 0
            value_100 = value
            quota_operation = quota_operation - value
            take_100 = 0
            print('po odjeciu value 100 ' + str(quota_operation))
            print("next operation 100\n")
        return value, quota_operation, take_100, value_100
    
    #SPRAWDZANIE 50-------------------------------------------------------------------------------------------------------------------50
    def spr_50(quota_operation, amount_50):

        #Czy w kwocie mieszczą sie 50 i ile
        if quota_operation // 50 > 0:
            quantity = quota_operation // 50 
            value = quantity * 50 
        else:
            quantity = 0
            value = quota_operation

        #Jeśli w bazie jest więcej lub tyle samo banknotów 
        if amount_50 >= quantity and amount_50 > 0:
            value = quantity * 50
            value_50 = value
            quota_operation = quota_operation - value
            take_50 = quantity
            print('do zabrania 50 ' + str(take_50))
        
        #Jeśli w bazie jest mniej banknotów
        elif amount_50 < quantity and amount_50 > 0:
            quantity = amount_50
            value = quantity * 50
            value_50 = value
            quota_operation = quota_operation - value
            take_50 = quantity
            print('do zabrania 50 ' + str(take_50))

        #Jeśli nie ma banknotów
        else:
            print('pierwsza kwota 50 ' + str(quota_operation))
            quantity = 0
            value = 0
            value_50 = value
            quota_operation = quota_operation - value
            take_50 = 0
            print('po odjeciu value 50 ' + str(quota_operation))
            print("next operation 50\n")    
        return value, quota_operation, take_50, value_50
    
    #SPRAWDZANIE 20-------------------------------------------------------------------------------------------------------------------20
    def spr_20(quota_operation, amount_20):

        #Czy w kwocie mieszczą sie 20 i ile
        if quota_operation // 20 > 0:
            quantity = quota_operation // 20 
            value = quantity * 20 
        else:
            quantity = 0
            value = quota_operation

         #Jeśli w bazie jest więcej lub tyle samo banknotów
        if amount_20 >= quantity and amount_20 > 0:
            value = quantity * 20
            value_20 = value
            quota_operation = quota_operation - value
            take_20 = quantity
            print('do zabrania 20 ' + str(take_20))

        #Jeśli w bazie jest mniej banknotów
        elif amount_20 < quantity and amount_20 > 0:
            quantity = amount_20
            value = quantity * 20
            value_20 = value
            quota_operation = quota_operation - value
            take_20 = quantity
            print('do zabrania 20 ' + str(take_20))
            
        #Jeśli nie ma banknotów
        else:
            print('pierwsza kwota 20 ' + str(quota_operation))
            quantity = 0
            value = 0
            value_20 = value
            quota_operation = quota_operation - value
            take_20 = 0
            print('po odjeciu value 20 ' + str(quota_operation))
            print("next operation 20\n")
        return value, quota_operation, take_20, value_20
    
    #SPRAWDZANIE 10-------------------------------------------------------------------------------------------------------------------10
    def spr_10(quota_operation, amount_10):

        #Czy w kwocie mieszczą sie 10 i ile
        if quota_operation // 10 > 0:
            quantity = quota_operation // 10 
            value = quantity * 10 
        else:
            quantity = 0
            value = quota_operation
        #Jeśli w bazie jest więcej lub tyle samo banknotów
        if amount_10 >= quantity and amount_10 > 0:
            value = quantity * 10
            value_10 = value
            quota_operation = quota_operation - value
            take_10 = quantity
            print('do zabrania 10 ' + str(take_10))

        #Jeśli w bazie jest mniej banknotów
        elif amount_10 < quantity and amount_10 > 0:
            quantity = amount_10
            value = quantity * 10
            value_10 = value
            quota_operation = quota_operation - value
            take_10 = quantity
            print('do zabrania 10' + str(take_10))
            
        
        #Jeśli nie ma banknotów
        else:
            print('pierwsza kwota 10 ' + str(quota_operation))
            quantity = 0
            value = 0
            value_10 = value
            quota_operation = quota_operation - value
            take_10 = 0
            print('po odjeciu value 10 ' + str(quota_operation))
            print("next operation 10\n")
        return value, quota_operation, take_10, value_10
    
    #Koniec---------------------------------------------------------------------------------------------------------------------------

    value, quota_operation, take_200, value_200 = spr_200(quota_operation, amount_200)
    value, quota_operation, take_100, value_100 = spr_100(quota_operation, amount_100)
    value, quota_operation, take_50, value_50 = spr_50(quota_operation, amount_50)
    value, quota_operation, take_20, value_20 = spr_20(quota_operation, amount_20)
    value, quota_operation, take_10, value_10 = spr_10(quota_operation, amount_10)

    sure_take_200 = take_200
    sure_take_100 = take_100
    sure_take_50 = take_50
    sure_take_20 = take_20
    sure_take_10 = take_10

    print('Taki')
    print(take_200)
    print(take_100)
    print(take_50)
    print(take_20)
    print(take_10)

    print('valuesy')
    print(value_200)
    print(value_100)
    print(value_50)
    print(value_20)
    print(value_10)
    print('suma')

    suma_value = value_200 + value_100 + value_50 + value_20 + value_10
#//////////////////////////////////////////////////////////////////////////////////
    # Jeśli kwota mniejsza od sumy w bazie
    diff_check = []
    diff_check.append(0)
    quota_operation = quota - suma_value
        
    if quota_operation > 0:
        amount_200 = amount_200 - take_200
        amount_100 = amount_100 - take_100
        amount_50 = amount_50 - take_50
        amount_20 = amount_20 - take_20
        amount_10 = amount_10 - take_10
        print('nowe amounty')
        print(amount_200)
        print(amount_100)
        print(amount_50)
        print(amount_20)
        print(amount_10)
        #dla 200
        value, quota_operation, take_200, value_200 = spr_200(quota_operation, amount_200)
        if amount_200 == 0:
            diff_200 = 1000
        else:
            diff_200 = abs(200 - quota_operation)
        diff_check.append(diff_200)

        #dla 100
        value, quota_operation, take_100, value_100 = spr_100(quota_operation, amount_100)
        if amount_100 == 0:
            diff_100 = 1000
        else:
            diff_100 = abs(100 - quota_operation)
        diff_check.append(diff_100)

        #dla 50
        value, quota_operation, take_50, value_50 = spr_50(quota_operation, amount_50)
        if amount_50 == 0:
            diff_50 = 1000
        else:
            diff_50 = abs(50 - quota_operation)
        diff_check.append(diff_50)

        #dla 20
        value, quota_operation, take_20, value_20 = spr_20(quota_operation, amount_20)
        if amount_20 == 0:
            diff_20 = 1000
        else:
            diff_20 = abs(20 - quota_operation)
        diff_check.append(diff_20)
        #dla 10
        value, quota_operation, take_10, value_10 = spr_10(quota_operation, amount_10)
        if amount_10 == 0:
            diff_10 = 1000
        else:
            diff_10 = abs(10 - quota_operation)
        diff_check.append(diff_10)


        print(diff_check)

        #Wybór najmniejszej różnicy
        least = min(diff_check)
        print(least)
        print('////')
        if least == diff_check[1]:
            sure_take_200 = sure_take_200 + 1

        elif least == diff_check[2]:
            sure_take_100 = sure_take_100 + 1

        elif least == diff_check[3]:
            sure_take_50 = sure_take_50 + 1

        elif least == diff_check[4]:
            sure_take_20 = sure_take_20 + 1

        elif least == diff_check[5]:
            sure_take_10 = sure_take_10 + 1

    print('sure')
    print(sure_take_200)
    print(sure_take_100)
    print(sure_take_50)
    print(sure_take_20)
    print(sure_take_10)

    sure_value = sure_take_200 * 200 + sure_take_100 * 100 + sure_take_50 * 50 + sure_take_20 * 20 + sure_take_10 * 10
    while True:
        question = input('Czy chcesz wypłacić kwotę ' + str(sure_value)+'zl ?\n Tak/Nie\n')
        if question == 'Nie':
            exit()
        if question == 'Tak':
            #Ponowne wyciągnięcie ilości banknotów w bazie danych
            sql = "SELECT ilosc FROM bankomat WHERE nominal = '200'"
            cursor.execute(sql)
            amount_200 = cursor.fetchone()[0]

            sql = "SELECT ilosc FROM bankomat WHERE nominal = '100'"
            cursor.execute(sql)
            amount_100 = cursor.fetchone()[0]

            sql = "SELECT ilosc FROM bankomat WHERE nominal = '50'"
            cursor.execute(sql)
            amount_50 = cursor.fetchone()[0]
            
            sql = "SELECT ilosc FROM bankomat WHERE nominal = '20'"
            cursor.execute(sql)
            amount_20 = cursor.fetchone()[0]

            sql = "SELECT ilosc FROM bankomat WHERE nominal = '10'"
            cursor.execute(sql)
            amount_10 = cursor.fetchone()[0]
            
            new_amount_200 = amount_200 - sure_take_200
            new_amount_100 = amount_100 - sure_take_100
            new_amount_50 = amount_50 - sure_take_50
            new_amount_20 = amount_20 - sure_take_20
            new_amount_10 = amount_10 - sure_take_10
            new_quota = acc_balance - sure_value

            # Update do bazy bankomat
            sql = "UPDATE bankomat SET ilosc = %s WHERE nominal='200'"
            cursor.execute(sql, (new_amount_200,))  

            sql = "UPDATE bankomat SET ilosc = %s WHERE nominal='100'"
            cursor.execute(sql, (new_amount_100,))
        
            sql = "UPDATE bankomat SET ilosc = %s WHERE nominal='50'"
            cursor.execute(sql, (new_amount_50,))
            
            sql = "UPDATE bankomat SET ilosc = %s WHERE nominal='20'"
            cursor.execute(sql, (new_amount_20,))
            
            sql = "UPDATE bankomat SET ilosc = %s WHERE nominal='10'"
            cursor.execute(sql, (new_amount_10,))
            
            #Update do bazy users
            sql = "UPDATE users SET bilans=%s WHERE numer_karty=%s"
            cursor.execute(sql, (new_quota, input_numer_karty))

            connection.commit()
            break
        else:
            continue
