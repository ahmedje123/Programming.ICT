tempCelsius = eval(input('Hoe warm is het in graden celsius?'))
tempFahrenheit = tempCelsius * 1.8 + 32

def convert(tempCelsius, tempFahrenheit):
    print('Het is ', tempCelsius ,'graden, dat is ', tempFahrenheit , 'Fahrenheit.')

convert(tempCelsius, tempFahrenheit)