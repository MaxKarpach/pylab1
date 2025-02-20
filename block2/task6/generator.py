import random

file = open("input.txt", "w")
n = random.randint(1, 10**3)

file.write(str(n) + '\n')
for number in range(n):
    file.write(str(random.randint(1, 10**9)) + ' ')

file.close()
