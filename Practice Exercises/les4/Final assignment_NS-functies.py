def standaardprijs(afstandKM):
    if afstandKM < 50:
        return (afstandKM * 80) / 100
    else:
        return ((afstandKM * 60) + 1500) / 100

def ritprijs(leeftijd, weekendrit, afstandKM):
    if weekendrit == 'true':
        if leeftijd < 12 or leeftijd > 64:
            prijs = (standaardprijs(afstandKM) * 0.65)
        else:
            prijs = (standaardprijs(afstandKM) * 0.60)

    elif weekendrit == 'false':
        if leeftijd < 12 or leeftijd > 64:
            prijs = (standaardprijs(afstandKM) * 0.70)
        else:
            prijs = standaardprijs(afstandKM)

    return prijs

print(ritprijs(40, 'false', 60))
print(standaardprijs(40))

print('Uw reis kost €' + str((ritprijs(int(input('wat is uw leeftijd?')), (input('Is het weekend? (antwoord true of false')), int((input('Hoeveel KM reist u?')))))))
