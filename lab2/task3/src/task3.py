import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(base_dir)

from utils import read_integers_from_file, write_array_to_file, measure_performance

def merge_and_count(arr, temp_arr, left, mid, right):
    i = left    
    j = mid + 1 
    k = left    
    inv_count = 0
    
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)  
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
        
    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count

def process_file(input_file_path, output_file_path):
    n, arr = read_integers_from_file(input_file_path)

    if not (1 <= n <= 10**5):
        raise ValueError("Значение n находится вне допустимого диапазона: 1 ≤ n ≤ 100000")

    if len(arr) != n:
        raise ValueError(f"Количество элементов в arr должно быть равно n: {n}.")

    for value in arr:
        if not (abs(value) <= 10**9):
            raise ValueError("Значение arr[i] находится вне допустимого диапазона: -10^9 ≤ arr[i] ≤ 10^9")

    temp_arr = [0] * n
    result = merge_sort_and_count(arr, temp_arr, 0, n - 1)
    write_array_to_file(output_file_path, [result])

def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task3'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    measure_performance(process_file, input_file_path, output_file_path)

if __name__ == "__main__":
    main()
