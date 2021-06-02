num = int(input("Enter a number  (0 end) : "))

smallest = num
biggest = num

while num != 0:
    num = int(input("Enter a number  (0 end) : "))

    if num < smallest:
        smallest = num
    elif num > biggest:
        biggest = num
print("Le plus petit nombre est " + str(smallest))
print("Le plus grand nombre est " + str(biggest))

