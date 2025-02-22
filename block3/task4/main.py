input_file = open("input.txt", "r")
n = int(input_file.readline())
numbers = list(map(int, input_file.readline().split()))
k = int(input_file.readline()) # я без понятия зачем эта переменная
k_numbers = list(map(int, input_file.readline().split())) #потом переименовать
input_file.close()

output_file = open("output.txt", "w")

def bin_find(number, numbers, n):
    poss = n//2
    while n > 0:
        if numbers[poss] == number:
            return poss
        elif n==1 and numbers[poss] != number:
            return -1

        n -= (n // 2)
        if numbers[poss] < number:
            poss += n//2
        elif numbers[poss] > number:
            poss -= n//2

for asked_number in k_numbers:
    output_file.write(str(bin_find(asked_number, numbers, n)) + ' ')

output_file.close()
