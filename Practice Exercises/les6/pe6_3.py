invoer = '5-9-7-1-7-8-3-2-4-8-7-9'
getallen = invoer.split('-')
getallen.sort()
getallen = [int(i) for i in getallen]
print(getallen)
print('De grootste waarde is: ' + str(max(getallen)) + ' en de kleinste waarde: ' + str(min(getallen)))
print('aantal getallen: ' + str(len(getallen)) + ' en de som van de getallen: ' + str(sum(getallen)))
print('Gemiddelde: ' + str(sum(getallen)/len(getallen)))