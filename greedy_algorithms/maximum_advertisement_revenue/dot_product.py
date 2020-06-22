#Uses python3
# Problem Introduction. You have 𝑛 ads to place on a popular Internet page. For each ad, you know how much is the
#                       advertiser willing to pay for one click on this ad. You have set up 𝑛 slots on your page and
#                       estimated the expected number of clicks per day for each slot. Now, your goal is to distribute
#                       the ads among the slots to maximize the total revenue.
# Task.                 Given two sequences 𝑎1,𝑎2,...,𝑎𝑛 (𝑎𝑖 is the profit per click of the 𝑖-th ad) and 𝑏1,𝑏2,...,𝑏𝑛
#                       (𝑏𝑖 is the average number of clicks per day of the 𝑖-th slot), we need to partition them into 𝑛
#                       pairs (𝑎𝑖,𝑏𝑗) such that the sum of their products is maximized.
# Input Format.         The first line contains an integer 𝑛, the second one contains a sequence of integers
#                       𝑎1,𝑎2,...,𝑎𝑛, the third one contains a sequence of integers 𝑏1,𝑏2,...,𝑏𝑛.
# Constraints.          1≤𝑛≤10^3; −10^5≤𝑎𝑖,𝑏𝑖≤10^5 for all 1≤𝑖≤𝑛.
# Output Format.        Output the maximum value of ∑︀ 𝑎𝑖𝑐𝑖, where 𝑐1, 𝑐2, . . . , 𝑐𝑛 is a permutation of 𝑏1,𝑏2,...,𝑏𝑛.

import sys
from functools import reduce

def max_dot_product(a, b):
    combined_sorted_list = zip(sorted(a), sorted(b))
    return reduce(dot_product_summer, combined_sorted_list, 0)

def dot_product_summer(total, a_b_tuple):
    a, b = a_b_tuple
    return total + a * b

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))

