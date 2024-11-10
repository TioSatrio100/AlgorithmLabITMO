import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(base_dir)

from utils import  read_input_file, write_array_to_file, measure_performance

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def process_file(input_file_path, output_file_path):
    arr, queries = read_input_file(input_file_path)
    n = len(arr)

    print(f"n (количество элементов в массиве): {n}")
    print(f"Массив arr: {arr}")
    
    if not (1 <= n <= 10**5):
        raise ValueError("Значение n находится вне допустимого диапазона: 1 ≤ n ≤ 10^5")
    
    for value in arr:
        if not (1 <= value <= 10**9):
            raise ValueError(f"Значение элемента {value} находится вне допустимого диапазона: 1 ≤ ai ≤ 10^9")
    
    k = len(queries)
    if not (1 <= k <= 10**5):
        raise ValueError("Значение k находится вне допустимого диапазона: 1 ≤ k ≤ 10^5")
    
    for query in queries:
        if not (1 <= query <= 10**9):
            raise ValueError(f"Значение запроса {query} находится вне допустимого диапазона: 1 ≤ bi ≤ 10^9")
    
    results = []
    for query in queries:
        result = binary_search(arr, query)
        results.append(result)

    write_array_to_file(output_file_path, results)

def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task4'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    measure_performance(process_file, input_file_path, output_file_path)

if __name__ == '__main__':
    main()

