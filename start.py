import users
import wyplata
import currentcash

print('Witaj w bankomacie\n Podaj swój login')
login = input()
print('Podaj PIN')
pin = input()

if pin == getattr(users, login)['pin']:
    print("Co chcesz zrobić (wyplac, stan konta, wyjdz)")
    action = input()

    if action == 'stan konta':
        print(getattr(users, login)['balance'])

    if action == 'wyplac':
        wyplata.cashout()
        
        print("chuj")
              
    if action == 'wyjdz':
        print("Wyjscie")

else:
    print('Nieprawidłowe dane logowania')


