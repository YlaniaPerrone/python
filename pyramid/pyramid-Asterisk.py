def add_character(array, character):

    if '.' in array:
        for index in reversed(range(len(l))):
        #for index in range(-1, (len(array) +1) * -1, -1):
            if array[index] ==  '.':
                break
        
        array[index] = character

    return array

# -- main --

l = [".", ".", ".", ".", ".", "."]

while '.' in l:
    l = add_character(l, "X")
    print(l)


