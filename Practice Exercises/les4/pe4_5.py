def kwadraten_som(grondgetallen):
    x = 0
    for getal in grondgetallen:
        if getal >= 0:
            x += getal ** 2

    return x

print(kwadraten_som([3, 5, 8, 7, -6]))