from random import choice


def choose_word(list):
    return choice(list)
    

def grid_init(word):

    border_line = ''
    for i in range(len(word)):
        border_line += '_ '
    return border_line


def play(list, letter):
    word = choose_word(list)
    grid = grid_init(word)
   
    return add_letter(letter, word)


def check(user_letter, word):

    letter_played =[]
    count = 0
    if user_letter in word:
        print(word)

        for letter in word:
            if user_letter == letter:
                count += 1
                print(letter)     
    else: letter_played.appened(user_letter)   
    print(letter_played) 
    return count
    # return grid


def add_letter(user_letter, word):
    for letter in word:
        if grid == 'letter':
            count += 1
            print(letter)     

    # return grid

data = ['accélérassions', 'organisatrice', 'vikings', 'paix']  

word = str(input('write a letter :'))

print(play(data,word))
