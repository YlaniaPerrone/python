for i in reversed(range(10)):
    for j in reversed(range(10)):
        print(" ", end="")
    for j in range(i+1):
        print( i, end=" ")
   
    print()

for i in range(10):
    for j in range(i):
        print(' ', end=' ')
    for j in range(10-i):
        print(j, end=' ')
    print()