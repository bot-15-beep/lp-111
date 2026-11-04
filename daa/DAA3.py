def fractional_knapsack(capacity, items):
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    profit = 0

    for p, w in items:
        if capacity >= w:
            capacity -= w
            profit += p
        else:
            profit += p * (capacity / w)
            break

    return profit

items = [(60, 10), (100, 20), (120, 30)]
capacity = 50

print("Maximum Profit:",
      fractional_knapsack(capacity, items))
