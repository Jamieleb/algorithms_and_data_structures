# Uses python3
# Task. The goal in this problem is to find the minimum number of coins needed to change the input value (an integer)
#       into coins with denominations 1, 5, and 10.
# Input Format. The input consists of a single integer 𝑚.
# Constraints. 1 ≤ 𝑚 ≤ 10^3 .
# Output Format. Output the minimum number of coins with denominations 1, 5, 10 that changes 𝑚.
import sys

def get_change(m):
    number_of_coins = 0
    coin_types= [10, 5, 1]
    for coin_type in coin_types:
        number_of_coins += int(m / coin_type)
        m = m % coin_type
    return number_of_coins

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
