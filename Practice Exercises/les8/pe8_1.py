bruin = {'Best', 'Beukenlaan', 'Eindhoven', 'Helmond \'t Hout', 'Helmond', 'Helmond Brouwhuis', 'Deurne'}
groen = {'Best', 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'}

print('De plaatsen waar beide trajecten langs gaan zijn: ' + str(bruin.intersection(groen)))
print('De plaatsen waar bruin wel langs gaat en groen niet: '+ str(bruin.difference(groen)))
print('Alle stations zijn: ' + str(bruin.union(groen)))