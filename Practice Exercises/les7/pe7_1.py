lijst = []
while True:
    getal = int(input('Geef een getal: '))
    if getal != 0:
        lijst.append(getal)
    else:
        print('Er zijn '+ str(len(lijst)) + ' getallen ingevoerd en de som van de getallen is: ' + str(sum(lijst)))
        break