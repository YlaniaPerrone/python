from random import randint

numAleatoire1 = randint(0,100)
numAleatoire2 = randint(0,100)

some = numAleatoire1 + numAleatoire2

num =None
count = 0
while num != some:
    num = int(input( str(numAleatoire1) + " + " + str(numAleatoire2 ) + " : "))
    count+= 1

print("Trouvé en " + str(count) + " tentative(s)")





