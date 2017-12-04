with open('input.txt', 'r') as input_file:
    instructions = input_file.readlines()


def sum_1(numbers):
    lowest = 1000000000000 
    highest = 0 
    for n in numbers:
        n = int(n)
        if n < lowest:
            lowest = n
        if n > highest:
            highest = n
    return highest - lowest

def sum_2(numbers):
    for n in numbers:
        n = int(n)
        for n_d in numbers:
            n_d = int(n_d)
            if n != n_d and n % n_d == 0:
                return n / n_d

sum = 0
for i in [i.rstrip() for i in instructions]:
    sum += sum_2(i.split())
    
print sum
    

