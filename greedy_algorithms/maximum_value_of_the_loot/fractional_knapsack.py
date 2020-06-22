# Uses python3
import sys
#
# Problem Introduction: A thief finds much more loot than his bag can fit. Help him to find the most valuable
#                       combination of items assuming that any fraction of a loot item can be put into his bag.
# Input Format: The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack.
#               The next 𝑛 lines define the values and weights of the items. The 𝑖-th line contains integers 𝑣𝑖 and
#               𝑤𝑖—the value and the weight of 𝑖-th item, respectively.
# Constraints. 1≤𝑛≤10^3, 0≤𝑊≤2·10^6; 0≤𝑣𝑖≤2·10^6, 0<𝑤𝑖≤2·10^6 for all 1≤𝑖≤𝑛. All the numbers are integers.
# Output Format. Output the maximal value of fractions of items that fit into the knapsack. The absolute value of the
#                difference between the answer of your program and the optimal value should be at most 10^-3. To ensure
#                this, output your answer with at least four digits after the decimal point (otherwise your answer,
#                while being computed correctly, can turn out to be wrong because of rounding issues)

def get_optimal_value(capacity, weights, values):
    value = 0.
    filled_weight = 0
    weight_value_list = list(zip(weights, values))
    weight_value_list.sort(key=lambda weight_value: weight_value[1] / weight_value[0], reverse=True)
    while filled_weight < capacity and len(weight_value_list) > 0:
        best_item_remaining = weight_value_list.pop(0)
        amount_added = min(best_item_remaining[0], capacity - filled_weight)
        filled_weight += amount_added
        value += amount_added * (best_item_remaining[1] / best_item_remaining[0])
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
