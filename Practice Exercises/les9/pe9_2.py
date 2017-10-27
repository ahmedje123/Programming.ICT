import datetime
import csv
bestand = 'inloggers.csv'
while True:
    naam = input("Wat is je achternaam? ")
    if naam == 'einde':
        break
    else:
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        with open(bestand, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow([datetime.date.today().strftime('%a %d %m %Y at '), naam, voorl, gbdatum, email])
