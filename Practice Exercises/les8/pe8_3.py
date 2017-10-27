def code(invoerstring):
    input = invoerstring
    resultaat = ''
    for letter in input:
        waarde = ord(letter)
        code = waarde + 3
        resultaat += str(chr(code))
    print(resultaat)

code('RutteAlkmaarDen Helder')