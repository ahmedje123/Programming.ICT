import csv
with open('artikels.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)
    duurste =0
    minste = 1000000
    totaal = 0
    for row in reader:
        prijs = row[4]
        voorraad = row[3]
        totaal += int(row[3])
        if float(prijs) > float(duurste):
            duurste = prijs
            duur = row
        if int(voorraad) < int(minste):
            minste = voorraad
            exemplaar = row
    print('Het duurste artikel is ' + duur[2] + ' en die kost ' + duur[4] + ' Euro')
    print('Er zijn slechts ' + exemplaar[3] + ' exemplaren in voorraad van het product met nummer ' + exemplaar[0])
    print('In totaal hebben wij ' + str(totaal) + ' produchten in ons magazijn liggen')