import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import read_money_from_file, write_array_to_file, measure_performance

def coin_exchange(money, k, coins, coin_limit=None):
    dp = [float('inf')] * (money + 1)
    dp[0] = 0

    if coin_limit:
        for i in range(1, money + 1):
            for coin, limit in zip(coins, coin_limit):
                for count in range(1, limit + 1):
                    if i >= coin * count:
                        dp[i] = min(dp[i], dp[i - coin * count] + count)
    else:
        for i in range(1, money + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[money] if dp[money] != float('inf') else -1

def process_file(input_file_path, output_file_path):
    money, k, coins, coin_limit = read_money_from_file(input_file_path)

    result = coin_exchange(money, k, coins, coin_limit)

    write_array_to_file(output_file_path, [result])


def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task1'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    measure_performance(process_file, input_file_path, output_file_path)

if __name__ == "__main__":
    main()


