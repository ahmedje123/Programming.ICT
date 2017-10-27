while True:
    woord = input('Geef een string van 4 letters in: ')
    if len(woord) == 4:
        print('Inlezen van correcte string: ' + woord + 'is geslaagd')
        break
    else:
        print(woord + 'heeft ' + str(len(woord)) + ' letters')