
import sys
import os


base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import read_integers_from_file, write_array_to_file, measure_performance

def insertion_sort_recursive(arr, n):
    if n <= 1:
        return arr

    insertion_sort_recursive(arr, n - 1)

    key = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > key: 
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key  

    return arr

def process_file(input_file_path, output_file_path):
    
    n, arr = read_integers_from_file(input_file_path)
    
   
    if not (1 <= n <= 1000):
        raise ValueError("Ошибка: Значение n находится вне допустимого диапазона: 1 ≤ n ≤ 1000")
    
    if len(arr) != n:
        raise ValueError(f"Ошибка: Количество элементов в arr должно совпадать с n: {n}.")
    
    if any(abs(x) > 10**9 for x in arr):
        raise ValueError("Ошибка: Значение arr[i] находится вне допустимого диапазона: -10^9 ≤ arr[i] ≤ 10^9")
    
    
    sorted_arr = insertion_sort_recursive(arr, n)
    
    
    write_array_to_file(output_file_path, sorted_arr)

def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task3'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    measure_performance(process_file, input_file_path, output_file_path)

if __name__ == "__main__":
    main()



