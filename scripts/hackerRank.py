def min_operations_to_equalize(prices, queries):
    result = []
    for target_price in queries:
        operations = sum(abs(target_price - price) for price in prices)
        result.append(operations)
    return result

n = 3
q = 4
prices = [1, 2, 3]
queries = [3, 2, 1, 5]


def min_operations_to_equalize_optimized(prices, queries):
    # Sort the prices array to optimize the calculation of operations
    sorted_prices = sorted(prices)
    result = []

    for target_price in queries:
        operations = 0
        # Calculate the operations for prices less than the target price
        for price in sorted_prices:
            if price < target_price:
                operations += target_price - price
            else:
                # Calculate the operations for prices greater than the target price
                operations += price - target_price
        result.append(operations)

    return result

print(min_operations_to_equalize(prices,queries))
print(min_operations_to_equalize_optimized(prices,queries))