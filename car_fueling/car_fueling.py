# python3
# Problem Introduction: You are going to travel to another city that is located 𝑑 miles away from your home city.
#                       Your car can travel at most 𝑚 miles on a full tank and you start with a full tank. Along your
#                       way, there are gas stations at distances stop1, stop2, . . . , stop𝑛 from your home city.
#                       What is the minimum number of refills needed?
# Input Format.         The first line contains an integer 𝑑. The second line contains an integer 𝑚. The third line
#                       specifies an integer 𝑛. Finally, the last line contains integers stop1, stop2, . . . , stop𝑛.
# Output Format.        Assuming that the distance between the cities is 𝑑 miles, a car can travel at most 𝑚 miles on a
#                       full tank, and there are gas stations at distances stop1 , stop2 , . . . , stop𝑛 along the way,
#                       output the minimum number of refills needed. Assume that the car starts with a full tank. If it
#                       is not possible to reach the destination, output −1.
# Constraints.          1≤𝑑≤10^5. 1≤𝑚≤400. 1≤𝑛≤300. 0<stop1 <stop2 <···<stop𝑛 <𝑑.

import sys

def compute_min_refills(distance, tank, stops):
    current_position, number_of_refills = 0, 0
    stops.insert(0, 0)
    stops.append(distance)
    while stops[current_position] < distance:
        last_position = current_position
        while stops[current_position] < distance and stops[current_position + 1] - stops[last_position] <= tank:
            current_position += 1
        if current_position == last_position:
            number_of_refills = -1
            break
        if stops[current_position] < distance:
            number_of_refills += 1

    return number_of_refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
