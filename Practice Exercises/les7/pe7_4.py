def ticker(filename):
    file = open(filename)
    lines = file.readlines()
    ticker = {}
    for line in lines:
        gegeven = line.split(':')
        ticker.update({gegeven[0]:gegeven[1]})
    return ticker
ticker('tickersymbool.txt')

if input('Enter C if you want to enter a company name and T if you want to enter a ticker symbool: ') == 'C':
    input = input('Enter Company name: ')
    print('Ticker symbol: ' + ticker('tickersymbool.txt')[input])
else:
    input = input('Enter Ticker symbol: ')
    for items in ticker('tickersymbool.txt').items():
        if items[1].rstrip() == input:
            print('Company name: ' + items[0])