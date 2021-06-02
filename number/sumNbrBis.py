from random import randint

liste = []

count = 0

for i in range(randint(2,5)):
    liste.append(randint(0, 20))
print(liste)

somme = sum(liste)

nbr = int(input("somme : "))
while  somme != nbr:
    nbr = int(input("somme : " ))
print("Trop fort heiinn !!!! 🙃")
