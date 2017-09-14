leeftijd = eval(input('Wat is je leeftijd?'))
paspoort = input('Ben je in bezit van een Nederlands paspoort?')

if leeftijd >= 18 and paspoort == 'ja':
    print('Gefeliciteerd, je mag stemmen!')
else:
    print('Helaas, je mag niet stemmen.')