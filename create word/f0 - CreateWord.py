from random import choice

def make_words(nbr):
    letters = ["a", "h", "k", "o", "n", "s", "t"]
    #letters = ["🍕", "🌮", "🍟", "🍜", "🎂",  "🥨"]

    word = ""

    for i in range(nbr):
        word = word + choice(letters)

    return word

d = int(input("nbr : "))

#word = make_words(d)

print(make_words(d))

