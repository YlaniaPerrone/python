n= int(input("Enter a num (2 à 10) : "))
while n > 10 or n < 2:
    n= int(input("Enter a num (2 à 10) :"))
r= (n*2)-2
for i in range(1, n+1):
    print (" "*r, end=" ")
    r-=2
    k=i-1
    for j in range(1, i+1):
        print (j, end=" ")
    for j in range(k, 0, -1):
        print (j, end=" ")
    print (" ")