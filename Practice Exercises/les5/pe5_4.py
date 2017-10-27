outfile = open("C:\\Users\\Ahmad\\PycharmProjects\\untitled\\Practice Exercises\\les5\\kaartnummers.txt", 'a')
import datetime

while True:
    h = input('Hoe heet de hardloper: ')
    if len(h) != 0:
        vandaag = datetime.datetime.today()
        s = vandaag.strftime ('%a %d %b %y, %H:%M:%S, ' + h + '\n')
        outfile.write(s)
        outfile.flush()
    else:
        break

outfile.close()