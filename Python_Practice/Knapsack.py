def knapsack(items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            item_weight, item_value = items[i - 1]
            if item_weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item_weight] + item_value)
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w, v = capacity, dp[n][capacity]
    for i in range(n, 0, -1):
        if v <= 0:
            break
        if v != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            v -= items[i - 1][1]
            w -= items[i - 1][0]

    selected_items.reverse()

    return dp[n][capacity], selected_items

def knapsack_print(items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            item_weight, item_value = items[i - 1]
            if item_weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item_weight] + item_value)
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Print the DP table
    for row in dp:
        print(row)

    selected_items = []
    w, v = capacity, dp[n][capacity]
    for i in range(n, 0, -1):
        if v <= 0:
            break
        if v != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            v -= items[i - 1][1]
            w -= items[i - 1][0]

    selected_items.reverse()

    return dp[n][capacity], selected_items

# Example usage
items = [(20,15), (15,10), (25,25), (10,8), (22,17), (12,13), (14,10), (7,5), (2,2), (4,3), (8,6), (17,15)]
max_value, selected_items = knapsack_print(items, 60)

print("Maximum value:", max_value)
print("Selected items:", selected_items)

#(10,15),(7,10),(12,25),(8,8),(17,17),(3,13),(18,19),(1,5)