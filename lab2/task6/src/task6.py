import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(base_dir)

from utils import measure_performance, read_data, write_output

def find_maximum_subarray(arr, low, high):
    if high == low:
        return low, high, arr[low]

    mid = (low + high) // 2

    left_low, left_high, left_sum = find_maximum_subarray(arr, low, mid)
    right_low, right_high, right_sum = find_maximum_subarray(arr, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum

def find_max_crossing_subarray(arr, low, mid, high):
    left_sum = float('-inf')
    total = 0
    max_left = mid

    for i in range(mid, low - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total
            max_left = i

    right_sum = float('-inf')
    total = 0
    max_right = mid + 1

    for j in range(mid + 1, high + 1):
        total += arr[j]
        if total > right_sum:
            right_sum = total
            max_right = j

    return max_left, max_right, left_sum + right_sum

def process_file(input_file_path, output_file_path):
    dates, prices = read_data(input_file_path)
    if prices:
        buy_index, sell_index, max_profit = find_maximum_subarray(prices, 0, len(prices) - 1)
        write_output(output_file_path, "Tesla", "2024-10-01 до 2023-10-15", dates[buy_index], dates[sell_index], max_profit)
    else:
        print("Предупреждение: Входной файл не содержит допустимых цен.")

def main():
    base_dir = 'task6'
    input_file_path = os.path.join(base_dir, 'input.txt')
    output_file_path = os.path.join(base_dir, 'output.txt')
    
    measure_performance(process_file, input_file_path, output_file_path)

if __name__ == "__main__":
    main()
