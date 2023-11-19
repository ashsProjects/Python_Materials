def calculate_optimal_i(predecessor, profit):
    n = len(profit)
    optimal_i = [0] * n

    for i in range(n):
        max_profit = profit[i]
        optimal_i[i] = -1  # Initialize optimal_i for the current item to -1 (no predecessor)

        for j in range(i):
            if predecessor[j] < i and profit[j] + profit[i] > max_profit:
                max_profit = profit[j] + profit[i]
                optimal_i[i] = j

        profit[i] = max_profit

    return optimal_i

def print_optimal_i(predecessor, profit):
    optimal_i = calculate_optimal_i(predecessor, profit)
    n = len(profit)
    total_profit = 0

    for i in range(n):
        if optimal_i[i] != -1:
            total_profit += profit[i]

    print("Optimal values for all items:")
    for i in range(n):
        if optimal_i[i] != -1:
            print(f"Item {i}: Optimal i = {optimal_i[i]}")

    print(f"Total profit: {total_profit}")

# Example usage:
predecessor = [0,0,0,1,1,1,3]  # Predecessors for items 0, 1, 2, 3, and 4
profit = [0,3,6,7,10,4,12,15]  # Profits for items 0, 1, 2, 3, and 4
print_optimal_i(predecessor, profit)
