def gemiddelde(getallen):
    return sum(getallen)/len(getallen)

zin = input("Type de zin waarvan je het gemiddelde wil: ")
woorden = zin.split()
berekening = [len(woord) for woord in woorden]

print('Het gemiddelde is: ', gemiddelde(berekening))

print(gemiddelde)

