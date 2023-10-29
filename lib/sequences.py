#!/usr/bin/env python3

def print_fibonacci(length):
    sequence =[0,1]
    if length < 2:
        print([]) if length == 0 else print([0])
        return
    while len(sequence) < length:
        sequence.append(sequence[-1]+sequence[-2])
    print(sequence)

