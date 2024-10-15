
import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(base_dir)

from utils import is_file_exists, read_integers_from_file, write_sorted_data_to_file, measure_performance

def insertion_sort_with_indices(arr):
   
    n = len(arr)
    indices = list(range(n))
    sorted_arr = arr[:]
    
    for i in range(1, n):
        key = sorted_arr[i]
        key_index = indices[i]
        j = i - 1
        
        while j >= 0 and key < sorted_arr[j]:
            sorted_arr[j + 1] = sorted_arr[j]
            indices[j + 1] = indices[j]
            j -= 1
            
        sorted_arr[j + 1] = key
        indices[j + 1] = key_index
    
    return indices, sorted_arr

def process_file(input_file_path, output_file_path):
    
   
    is_file_exists(input_file_path)

    
    n, u_arr = read_integers_from_file(input_file_path)
    
    
    if 1 <= n <= 10**3 and len(u_arr) == n:
        if all(abs(value) <= 10**9 for value in u_arr):
            result_indices, sorted_arr = insertion_sort_with_indices(u_arr)
            
            
            write_sorted_data_to_file(output_file_path, result_indices, sorted_arr)
        else:
            print("Ошибка: Значения u_arr[i] находятся вне допустимого диапазона: -10^9 ≤ u_arr[i] ≤ 10^9.")
    else:
        print("Ошибка: Значение n должно быть в диапазоне 1 ≤ n ≤ 1000 и количество элементов должно совпадать с n.")

def main():
    base_dir = 'task2(prod)'
    input_file_path = os.path.join(base_dir,  'input.txt')
    output_file_path = os.path.join(base_dir, 'output.txt')
    
    
    measure_performance(process_file, input_file_path, output_file_path)

if __name__ == "__main__":
    main()


