import sys
import os


base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import read_integers_from_file, write_array_to_file, measure_performance

def insertion_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

def process_file(input_file_path, output_file_path):
    n, u_arr = read_integers_from_file(input_file_path)

    if not (1 <= n <= 10**3):
        raise ValueError("Значение n находится вне допустимого диапазона: 1 ≤ n ≤ 1000")

    if len(u_arr) != n:
        raise ValueError(f"Количество элементов в u_arr должно быть равно n: {n}.")

    for value in u_arr:
        if not (abs(value) <= 10**9):
            raise ValueError("Значение u_arr[i] находится вне допустимого диапазона: -10^9 ≤ u_arr[i] ≤ 10^9")

    result = insertion_sort(u_arr)
    write_array_to_file(output_file_path, result)

def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task1'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    measure_performance(process_file, input_file_path, output_file_path)


if __name__ == "__main__":
    main()

