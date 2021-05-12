def delete_vowel(word):
    
    liste =  ("a", "e", "i", "o", "u", "y")

    for vowel in liste:
        #if vowel in word:
        word = word.replace(vowel, "")
                    
    return word


word = input("mot : ")

print(delete_vowel(word))