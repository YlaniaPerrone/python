number = []



for i in range(11):
    for j in range(i):
        print(i, end=' ')
    print()

print("-- or --")


for n in range(11):
    for i in range(n):
        print(i, end=' ')
    print()


print("-- or --")

number = []
for i in range(10):
    number.append(str(i))
    for i in range(1):

        print(" ".join(number))
        

