maandnummer = eval(input('Hoeveelste maand van het jaar is het (in nummers)? '))

def seizoen(maandnummer):

    if 3 <= maandnummer <= 5:
        print('Het is nu lente')
    elif 6 <= maandnummer <= 8:
        print('Het is nu zomer')
    elif 9 <= maandnummer <= 11:
        print('Het is nu herfst')
    elif maandnummer == 12:
        print('Het is nu winter')
    elif maandnummer <= 2:
        print('Het is nu winter')
   

print(seizoen(maandnummer))
