def namen():
    namen = []
    while True:
        naam = input('Volgende naam: ')
        if naam == '':
            break
        else:
            namen.append(naam)
    resultaat = {}
    for naam in namen:
        resultaat.update ({naam : namen.count(naam)})
    for item in resultaat.items():
        if item[1] == 1:
            print('Er is 1 student met de naam ' + item[0])
        else:
            print('Er zijn ' + str(item[1]) + ' studenten met de naam ' + item[0])

namen()