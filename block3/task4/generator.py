import random

n = random.randint(1, 10**5)
file = open("input.txt", "w")
file.write(str(n) + '\n')

number = 0
for i in range(n):
    number += random.randint(1,100)
    file.write(str(number) + ' ')
file.write('\n')

k = random.randint(1, 10**5)
file.write(str(k) + '\n')

for j in range(k):
    file.write(str(random.randint(1,10**9)) + ' ')

file.close()
