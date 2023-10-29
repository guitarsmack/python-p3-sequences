#!/usr/bin/env python3
print("This works")

def print_fibonacci(length):
    if length < 2:
        print([]) if length == 0 else print([0])
        return
    sequence =[0,1]
    while len(sequence) < length:
        num1 = sequence[-1]
        num2 = sequence[-2]
        sequence.append(num1+num2)
    print(sequence)
    pass


print_fibonacci(2)