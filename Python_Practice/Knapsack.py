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

def knapsack_2(weights, values, capacity):
    n = len(values)
    table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                table[i][w] = max(values[i - 1] + table[i - 1][w - weights[i - 1]], table[i - 1][w])
            else:
                table[i][w] = table[i - 1][w]

    # Printing the table
    for row in table:
        print(row)

    # Backtracking to find selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if table[i][w] != table[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    selected_items.reverse()
    return table[n][capacity], selected_items

#For knapsack and knapsack_print
items = [(15,20), (10,15), (22,25), (13,13), (20,17), (12,13), (14,10), (7,5), (2,4), (4,5), (8,9), (17,15)]
max_value, selected_items = knapsack_print(items, 72)
print("Maximum value:", max_value)
print("Selected items:", selected_items)

#(9,10), (11,12), (13,15), (4,3), (10,12), (22,24), (12,13), (14,19), (7,8), (2,4), (8,9), (17,17)