from random import choice, randbytes


def choose_word(list):
    return choice(list)


def grid_init(word):
    # border_line = []
    # border_line += '_' * len(word)
    # return border_line

    border_line = []
    for i in range(len(word)):
        border_line += '_'
    return border_line


def checkCharacterInWord(character, word, border_line):
    for i in range(len(word)):
        if word[i] == character:
            border_line[i] = character

    return border_line


def play():

    print("\n----- Hangman's Game -----\n")
    print('Find the name \n')
    tries = 6

    #chooce word
    word = choose_word(data)
    print(word)

    # show - according to the number of letters
    grid = grid_init(word)

    while '_' in grid and tries > 0:
        print(display_hangman(tries))

        print(" ".join(grid))
        print("Remainder " + str(tries) + " tries ")

        character = input('write a character : ').lower()[0]

        if character in word:
            checkCharacterInWord(character, word, grid)

        else:
            tries -= 1

    if '_' in grid:
        print('\nPwa Pwa Pwa 😈', '\nthe word was ' + str(word))
    else:
        print('\n' + str(word) )
        print('\nBingoo 🤪🥳')
        print("You win in " + str(tries) + " tries")

def display_hangman(tries):
    stages = ["""
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / \\
       -
       """,
              """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     /
       -
       """,
              """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |
       -
       """,
              """
       --------
       |      |
       |      O
       |     \\|
       |      |
       |
       -
       """,
              """
       --------
       |      |
       |      O
       |      |
       |      |
       |
       -
       """,
              """
       --------
       |      |
       |      O
       |
       |
       |
       -
       """,
              """
       --------
       |      |
       |      
       |
       |
       |
       -
       """
              ]
    return stages[tries]


data = ['Julian', 'Kaezly', 'Nelia', 'Cayden', 'Sadou']


play()
