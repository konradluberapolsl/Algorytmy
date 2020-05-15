import os
def read(name):
    file = open(name, "r")
    numbers = file.read().splitlines()
    file.close()
    return numbers

def find_max(numbers):
    max = 0.0
    for i in range(len(numbers)):
        if i == 0: max = float(numbers[i])
        if float(numbers[i])>max: max = float(numbers[i])
    print(max)

find_max(read("Zad1/Zad1.1.txt"))