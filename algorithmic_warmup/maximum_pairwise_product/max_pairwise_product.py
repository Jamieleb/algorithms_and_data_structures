# python3
import functools

def reducer(max_dict, num):
    if num > max_dict[2]:
        if num > max_dict[1]:
            max_dict[2] = max_dict[1]
            max_dict[1] = num
        else:
            max_dict[2] = num
    return max_dict

def fast_max_pairwise_product(numbers):
    max_dict = functools.reduce(reducer, numbers, { 1: 0, 2: 0 }) 
    return max_dict[1] * max_dict[2]


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(fast_max_pairwise_product(input_numbers))
