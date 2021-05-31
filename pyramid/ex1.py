#Problem 1:
from typing import Counter

for n in range(10):
    for i in range(10):
        print(i, end=" ")
    print()

print("-- or --")
number = []


for i in range(10):
    number.append(str(i))
for i in range(10):

    print(" ".join(number))




