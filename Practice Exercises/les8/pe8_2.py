import random
def monopolyworp():
        while True:
                getal1 = random.randrange(1,7)
                getal2 = random.randrange(1,7)
                totaal = getal1 + getal2
                if getal1 == getal2:
                    print(str(getal1) + '+' + str(getal2) + '=' + str(totaal))
                    getal1 = random.randrange(1, 7)
                    getal2 = random.randrange(1, 7)
                    totaal = getal1 + getal2
                    if getal1 == getal2:
                        print(str(getal1) + '+' + str(getal2) + '=' + str(totaal))
                        getal1 = random.randrange(1, 7)
                        getal2 = random.randrange(1, 7)
                        totaal = getal1 + getal2
                        if getal1 == getal2:
                            print('Je gaat naar de gevangenis!')
                            break
                        else:
                            print(str(getal1) + '+' + str(getal2) + '=' + str(totaal))
                            break
                    else:
                        print(str(getal1) + '+' + str(getal2) + '=' + str(totaal))
                        break
                else:
                    print(str(getal1) + '+' + str(getal2) + '=' + str(totaal))
                    break

monopolyworp()