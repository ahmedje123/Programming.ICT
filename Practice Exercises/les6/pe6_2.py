lijst = ['woord', 'Testwoord', 'zetten', 'koe', 'papier', 'vijf', 'honderd', 'boter', 'kaas', 'eieren']
inputlijst =eval(input('Geef lijst met minimaal 10 strings: '))
for woord in inputlijst:
    if len(woord) == 4:
        print(woord)
