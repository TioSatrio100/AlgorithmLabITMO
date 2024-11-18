import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import measure_performance, read_data, write_output

def find_maximum_subarray(arr):
    max_sum = float('-inf')
    current_sum = 0
    start = 0
    end = 0
    temp_start = 0

    for j in range(len(arr)):
        current_sum += arr[j]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = j

        if current_sum < 0:
            current_sum = 0
            temp_start = j + 1

    return start, end, max_sum

def process_file(input_file_path, output_file_path):
    dates, prices = read_data(input_file_path)
    if prices:
        buy_index, sell_index, max_profit = find_maximum_subarray(prices)
        write_output(output_file_path, "Tesla", "2024-10-01 до 2024-10-15", dates[buy_index], dates[sell_index], max_profit)
    else:
        print("Предупреждение: Входной файл не содержит допустимых цен.")

def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task7'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    measure_performance(process_file, input_file_path, output_file_path)

if __name__ == "__main__":
    main()
