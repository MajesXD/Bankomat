# import users
# import start

def cashout ():
    cash = int(input('Wpisz kwotę do wypłaty '))
    while True:
        if cash % 10 == 0:
            a = True
        else:
            a = False

        if cash <= 500:
            b = True
        else:
            b = False

        if a == True and b == False:
            print('Maksymalna kwota do wypłaty to 500zł')
            cash = int(input('Wpisz kwotę do wypłaty '))
            
        elif a == False and b == True:
            print('Kwota musi być podzielna przez 10')
            cash = int(input('Wpisz kwotę do wypłaty '))

        elif a == False and b == False:
            print('Kwota musi być podzielna przez 10 i wynosić maksymalnie 500zł')
            cash = int(input('Wpisz kwotę do wypłaty '))

        elif cash == 0:
            print('Kwota musi być różna od 0')
            cash = int(input('Wpisz kwotę do wypłaty '))

        elif a == True and b == True:
            print(cash)
            break