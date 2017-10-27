infile = open("C:\\Users\\Ahmad\\PycharmProjects\\untitled\\Practice Exercises\\les5\\kaartnummers.txt", 'r')
content = infile.read()
infile.close()

list = [line.split(', ') for line in content.split('\n')]

for i in list:
    print(i[1] + ' heeft kaartnummer: ' + i[0])

