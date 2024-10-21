import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(base_dir)


from utils import  read_integers_from_file, write_array_to_file, measure_performance

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)
  
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

       
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

def process_file(input_file_path, output_file_path):
    n, arr = read_integers_from_file(input_file_path)

    if not (1 <= n <= 10**3):
        raise ValueError("Значение n находится вне допустимого диапазона: 1 ≤ n ≤ 1000")

    if len(arr) != n:
        raise ValueError(f"Количество элементов в u_arr должно быть равно n: {n}.")

    for value in arr:
        if not (abs(value) <= 10**9):
            raise ValueError("Значение u_arr[i] находится вне допустимого диапазона: -10^9 ≤ u_arr[i] ≤ 10^9")

    result = merge_sort(arr)
    write_array_to_file(output_file_path, result)

def main():
    base_dir = 'task1'
    input_file_path = os.path.join(base_dir,  'input.txt')
    output_file_path = os.path.join(base_dir, 'output.txt')
    measure_performance(process_file, input_file_path, output_file_path)

if __name__ == "__main__":
    main()






