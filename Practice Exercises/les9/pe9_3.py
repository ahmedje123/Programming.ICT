import csv
with open('gamers.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    topscore = 0
    for row in reader:
        score = row[2]
        if int(score) > int(topscore):
            topscore = score
            resultaat = row
    print('De hoogste score is: ' + resultaat[2] + ' op ' + resultaat[1] + ' behaalt door ' + resultaat[0])