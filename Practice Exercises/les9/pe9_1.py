try:
    prijs = 4356
    personen = int(input('Hoeveel personen: '))
    if personen < 1:
        print('Negatieve getallen zijn niet toegestaan!')
    else:
        result = prijs / personen
        print(result)
except ZeroDivisionError:
    print('Delen door nul kan niet!')
except ValueError:
    print('Gebruik cijfers voor het invoeren van het aantal!')
except:
    print('Onjuiste invoer!')

