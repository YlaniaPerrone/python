from random import randint

count = 1

nbr = int(input("nombre entre 2 et 5: "))
while nbr < 2 or nbr > 5 :
    nbr = int(input("nombre entre 2 et 5: "))

liste = []

for i in range(nbr):
    liste.append(randint(0, 20))
print(liste)

somme = sum(liste)
print(somme)

guess = int(input(" somme : "))

while guess != somme:
    guess = int(input(" somme : "))
    count += 1

print("bingo, vous avez réussi en " + str(count) + " essaies")