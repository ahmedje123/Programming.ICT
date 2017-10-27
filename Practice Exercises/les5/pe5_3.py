infile = open("C:\\Users\\Ahmad\\PycharmProjects\\untitled\\Practice Exercises\\les5\\kaartnummers.txt", 'r')
content =  infile.read()
lst = [line.split(', ')[0] for line in content.split ('\n')]
x = max(lst)
infile.close()

print('Deze file telt ' , len(lst) , ' regels')
print('Het grootste kaarntummer is: ', x , ' en dat staat op regel ' , lst.index(x) + 1)