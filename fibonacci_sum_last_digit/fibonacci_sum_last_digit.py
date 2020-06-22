# Uses python3
# Task. Given an integer 𝑛, find the last digit of the sum 𝐹0 +𝐹1 +···+𝐹𝑛.
# Input Format. The input consists of a single integer 𝑛.
# Constraints. 0 ≤ 𝑛 ≤ 10^14.
import sys

# Use pisano period to fine last digit more efficiently. Pisano period is 60 for mod 10

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
    return fibonacci(n % 60) % 10

def fibonacci_sum(n):
    if n <= 1:
        return n

    sum = 1



    return sum

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    print(fibonacci_sum(n))
