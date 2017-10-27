def inlezen_beginstation(stations):
    while True:
        station = input('Wat is je beginstation: ')
        if station in stations:
            return station
        else:
            print('Dit stations bestaat niet')

def inlezen_eindstation(stations, beginstation):
    while True:
        station = input('Wat is je eindstation: ')
        if station in stations and stations.index(station) > stations.index(beginstation):
            return station
        elif station in stations and stations.index(station) <= stations.index(beginstation):
            print('De trein komt niet meer langs dit station')
        else:
            print('Dit station bestaat niet!')

def omroepen_reis(stations, beginstation, eindstation):
    print('Het beginstation ' + beginstation + ' is het ' + str(stations.index(beginstation) + 1) + 'e station in het traject')
    print('Het beginstation ' + eindstation + ' is het ' + str(stations.index(eindstation) + 1) + 'e station in het traject')
    print('De afstand is ' + str(stations.index(eindstation)-stations.index(beginstation)) +' station(s)')
    print('De prijs van het kaartje is ' + str((stations.index(eindstation)-stations.index(beginstation)) * 5) + ' euro')
    print('Je stapt in de trein in: ' + beginstation)
    for x in stations:
        if stations.index(eindstation) > stations.index(x) > stations.index(beginstation):
            print('    - ' + x)
    print('Je stapt uit in: ' + eindstation)


stations = ['Schagen', 'Heerhugowaard', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)


