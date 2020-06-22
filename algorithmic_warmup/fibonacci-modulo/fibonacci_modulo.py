# Uses python3

# Task. Given two integers 𝑛 and 𝑚, output 𝐹𝑛 (the fibonacci sequence result as index n) mod 𝑚
# Input Format. The input consists of two integers 𝑛 and 𝑚 given on the same line (separated by a space).
# Constraints. 1≤𝑛≤10^14 ,2≤𝑚≤10^3.

import sys

def fibonacci(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current

def pisano_period(m):
    previous = 0
    current = 1

    period = 2
    while True:
        previous, current = current, fibonacci(period) % m

        if previous == 0 and current == 1:
            return period - 1
        period += 1

def fibonacci_modulo(n, m):
    return fibonacci(n % pisano_period(m)) % m

if __name__ == '__main__':
    input = sys.stdin.readline();
    n, m = map(int, input.split())
    print(pisano_period(n))
