from random import randint
'''
liste = []

count = 0
somme = []
while True:
    for i in range(3):
        liste.append( randint(1, 6) )
        
    if liste[0] == liste[1] and liste[1] == liste[2]:
        sum(liste)
        break
    count +=1 
    print(liste)

    liste.clear()
print(liste, sum(liste) )
'''

#***********Version easy***********#

liste = [randint(1,6), randint(1,6), randint(1,6)]

while liste[0] != liste[1] or liste[1]!= liste[2]:
    liste = [randint(1,6), randint(1,6), randint(1,6)]
print(liste)