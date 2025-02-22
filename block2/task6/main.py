import time
t_start = time.perf_counter()

input_file = open("input.txt", "r")
n = input_file.readline()
numbers = input_file.readline().split()
input_file.close()

for i in range(int(n)-1):
    for j in range(int(n)-i-1):
        if numbers[j] > numbers[j+1]:
            replace = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = replace

output_file = open("output.txt", "w")
for number in numbers:
    output_file.write(str(number) + ' ')
output_file.close()

print("Time spend: %s seconds." % (time.perf_counter() - t_start))
