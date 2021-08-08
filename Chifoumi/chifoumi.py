from random import choice

array = ["pierre", "papier", "ciseaux"]
rep = None

user = None

while rep != "n":
    choose = input("Faites vos jeux  (pierre, papier, ciseaux) : ")

    if choose in array:
        # user = input("Faites vos jeux : ")
        print("vous : " + str(choose))

        ordi = choice(list(array))
        print("ordi : " + str(ordi))

        if ordi == "pierre" and user == "ciseaux" or ordi == "ciseaux" and user == "papier" or ordi == "papier" and user == "pierre":
            print(" - perdu")
            rep = input("Voulez vous recommencé n/o : ")

        if ordi == user:
            print("égalité")

        # elif ordi == "pierre" and user == "papier" or ordi == "ciseaux" and user == "pierre" or ordi == "papier" and user == "ciseaux":
        # print("gagné")
        # rep = input("Voulez vous recommencé n/o : ")

        else:
            print("égalité")
            rep = input("Voulez vous recommencé n/o : ")

print("fin de jeu")

"""
array = {
    "pierre": "👊",
    "papier": "🤚",
    "ciseaux": "✌",
}


user = input("Faites vos jeux : ")

while user not in array.keys():
    user = input("Faites vos jeux : ")
print("vous : " + str(array[user])) # récupére valeur 

ordi = choice(list(array.keys()))
print("ordi : " + str(array[ordi]))


if ordi == "pierre" and user == "ciseaux" or ordi == "ciseaux" and user == "papier" or ordi == "papier" and user == "pierre":      
    print(" - perdu")

elif ordi == "pierre" and user == "papier" or ordi == "ciseaux" and user == "pierre" or ordi == "papier" and user == "ciseaux":     
    print("gagné")

else : 
    print("égalité")
    """