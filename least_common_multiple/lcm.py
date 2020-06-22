# Uses python3

# Task. Given two integers 𝑎 and 𝑏, find their least common multiple.
# Input Format. The two integers 𝑎 and 𝑏 are given in the same line separated by space.

import sys

def lcm(a, b):
    for multiple in [a * num for num in range(1, b + 1)]:
        if multiple % b == 0:
            return multiple

if __name__ == '__main__':
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(lcm(a, b))

