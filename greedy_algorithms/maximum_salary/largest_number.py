#Uses python3
# Problem Introduction  As the last question of a successful interview, your boss gives you a few pieces of paper with
#                       numbers on it and asks you to compose a largest number from these numbers. The resulting number
#                       is going to be your salary, so you are very much interested in maximizing this number.
#                       How can you do this?
# Task.                 Compose the largest number out of a set of integers.
# Input Format.         The first line of the input contains an integer 𝑛. The second line contains integers
#                       𝑎1,𝑎2,...,𝑎𝑛.
# Constraints.          1 ≤ 𝑛 ≤ 100; 1 ≤ 𝑎𝑖 ≤10^3 for all 1 ≤ 𝑖 ≤ 𝑛.
# Output Format.        Output the largest number that can be composed out of 𝑎1, 𝑎2, . . . , 𝑎𝑛.

import sys

def largest_number(a):
    res = ""
    while a:
        largest_number = '0'
        for index, num in enumerate(a):
            if is_greater_or_equal(num, largest_number):
                largest_number = num
                largest_number_index = index
        res += a.pop(largest_number_index)
    return res

def is_greater_or_equal(num, largest_number):
    concat1, concat2 = num + largest_number, largest_number + num
    if int(concat2) > int(concat1):
        return False
    return True

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

