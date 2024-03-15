import time


def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in sorted(coins, reverse=True):
        count = amount // coin
        if count > 0:
            result[coin] = count
        amount %= coin
    
    return result



def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    min_coins_count = [float("inf")] * (amount + 1)
    min_coins_count[0] = 0

    for coin in coins:
        for current_amount in range(coin, amount + 1):
            min_coins_count[current_amount] = min(min_coins_count[current_amount], min_coins_count[current_amount - coin] + 1)

    # Reconstruct the result
    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = max(coin for coin in coins if current_amount - coin >= 0 and min_coins_count[current_amount] == min_coins_count[current_amount - coin] + 1)
        result[coin] = result.get(coin, 0) + 1
        current_amount -= coin

    return result
         
                
if __name__ == "__main__":
    amount = 113

    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start_time

    start_time = time.time()
    min_coins_result = find_min_coins(amount)
    min_coins_time = time.time() - start_time

    print("Greedy Algorithm Result:", greedy_result)
    print("Greedy Algorithm Time:", greedy_time)

    print("Dynamic Programming Result:", min_coins_result)
    print("Dynamic Programming Time:", min_coins_time)

