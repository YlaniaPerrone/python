def display_board(current_board):

    for i in range(5):
        # Créer une chaine de caractères
        board_line = str(i)
        # Parcourir la ligne i de game_board
        # Pour chaque élément de la ligne
        for element in current_board[i]:
            # L'ajouter à la fin de board_line
            board_line = board_line + " " + element

        print(board_line)

    print("  0 1 2 3 4")


def play(game_board, player):
 
    column = int(input("Player " + str(player) + " : which column ? (0-4) "))

    game_board = add_token(game_board, player, column)
   
    return check(game_board, column)
    

def add_token(grid, player_id, col):
  
    if player_id == 1:
        token = "O"
    else:
        token = "X"  

    for index in range(4, -1, -1):
        if grid[index][col] == ".":
            grid[index][col] = token
            break

    return grid


def check(grid, col):
    
    # for l in range(len(grid)):   
        #if grid[l][col] != ".":
            #break
            #if  grid[l][col] == grid[l+1][col] == grid[l+2][col]:
                #print(grid[l][col])
                #return True
            #else:
                #return False
    
    for index in range(5):   
        #if add_token(grid, player_id, col):
        if grid[index][col] != ".":
            print(grid[index][col])
            break
    print("index : " + str(index))

    if check_vertical(grid, index, col):
        return True
    
    if check_horizontal(grid, index, col):
        return True
    
    if check_diago(grid, index, col):
        return True

    return False


def check_vertical(grid, line, col):

    if line < 3:
        if grid[line+1][col] == grid[line][col] and grid[line+2][col] == grid[line][col]:
            return True

    return False

def check_horizontal(grid, line, col):
    print("col : " + str(col) + " line : " + str(line))
    
    if col < 3:
        if grid[line][col+1] == grid[line][col] and grid[line][col+2] == grid[line][col]:
            return True
    if col > 1:
        if grid[line][col-1] == grid[line][col] and grid[line][col-2] == grid[line][col]:
           return True
    if col > 0 and col < 4:
        if grid[line][col-1] == grid[line][col] and grid[line][col+1] == grid[line][col]:
           return True

    return False


def check_diago(grid, line, col):
    #diagonale descend
    if col < 3 and line < 3:
        if grid[line+1][col+1] == grid[line][col] and grid[line+2][col+2] == grid[line][col]:
            return True
    if col > 1 and line > 1:
        if grid[line-1][col-1] == grid[line][col] and grid[line-2][col-2] == grid[line][col]:
            return True
    if col > 0 and col < 4 and line > 0 and line < 4:
        if grid[line-1][col-1] == grid[line][col] and grid[line+1][col+1] == grid[line][col]:
            return True
    
    #diagonale monte
    if col in range(3,1) and line in range(3,1):
        if grid[line-1][col+1] == grid[line][col] and grid[line-2][col+2] == grid[line][col]:
            return True
    if col in range(3,1) and line in range(3,1):
        if grid[line+1][col-1] == grid[line][col] and grid[line+2][col-2] == grid[line][col]:
            return True
    if col in range(4,0) and line in range(4,0):
        if grid[line-1][col+1] == grid[line][col] and grid[line+1][col-1] == grid[line][col]:
            return True
    return False
   


board = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."]
]

winner = None
player = 1

while winner == None:
    # Afficher le tableau
    display_board(board)

    # Faire jouer le joueur
    if play(board, player):
        # On a un vainqueur
        winner = player
    else:
        # Si pas de vainqueur, changer de joueur
        if player == 1:
            player = 2
        else:
            player = 1

display_board(board)
print("Congratulations! Player " + str(winner) + " won the game!")



