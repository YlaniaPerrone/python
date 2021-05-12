from random import randint

nbr =  int(input(" nombre : "))
array = []

fibbo = [1,2]

while nbr < 1 :
    nbr =  int(input(" nombre : "))

for i in range(nbr - 2):
    new = fibbo[-1] + fibbo[-2]
    fibbo.append(new)
    
display = ""

for n in fibbo:
    display = display + str(n)+", "

display = display[:-2]

print(display)
