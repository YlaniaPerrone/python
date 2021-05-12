from random import choice


list_word = ['accelerassions', 'organisatrice', 'vikings', 'paix']  

word = choice(list_word)

border_line = []
for i in range(len(word)):
    border_line.append(' _ ')

print("".join(border_line))

print(word)


letter_wrong = []
count = 10
#count = len(word)
print(count)


while  ' _ ' in border_line and count > 0:
    letter = str(input("Write a character : "))

    while len(letter) != 1:
    
        letter = str(input("Write 1 character : "))
        
    if letter in word:
        for i in range(len(word)):
            if word[i] in letter:
                border_line[i] = letter
                #print(i)
   
    else: 
        count -= 1
        letter_wrong.append(letter)
        

    
    print("".join(border_line))
    print("wrong character " + str(letter_wrong) )
    print("il te reste " + str(count) + " essaies ")

if count == 0 and ' _ ' in border_line:
    print('Pwa Pwa Pwa 😈')
else:
    print('bingoo 🤪🥳')
