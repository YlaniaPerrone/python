'''
from random import randint

code = []

#addLetter = str(input("Entrez une lettre : "))
sizeMax = 4

while len(code) != sizeMax:
    
    index = randint(0,sizeMax)
    print(index)

    code.append(index)
    print(code)

    #break
'''
from random import randint
letters = ["😋", "🤣", "🤪", "😅", "😘", "😊"]

code = []

#addLetter = str(input("Entrez une lettre : "))
sizeMax = 4

while len(code) != sizeMax:
    
    index = randint(0,len(letters)-1)
    code.append(letters[index])

print(code)

