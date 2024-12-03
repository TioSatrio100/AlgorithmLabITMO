from utils import read_integers_from_file, write_array_to_file, measure_performance
import sys
import os
import random

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)


'''
#standard quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr 
    else:
       pivot = arr[len(arr) // 2]
       left = [x for x in arr if x < pivot]
       middle = [x for x in arr if x == pivot]
       right = [x for x in arr if x > pivot]
       return quick_sort(left) + middle + quick_sort(right)
'''

# standard randomized quick sort with 3-way partitioning


def randomized_quick_sort(arr, low, high):
    if low >= high:
        return

    pivot_index = random.randint(low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
    pivot = arr[low]

    lt = low
    gt = high
    i = low

    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
        else:
            i += 1

    randomized_quick_sort(arr, low, lt - 1)
    randomized_quick_sort(arr, gt + 1, high)

    return arr


def process_file(input_file_path, output_file_path):
    n, arr = read_integers_from_file(input_file_path)

    if not (1 <= n <= 10**3):
        raise ValueError(
            "Значение n находится вне допустимого диапазона: 1 ≤ n ≤ 1000")

    if len(arr) != n:
        raise ValueError(
            f"Количество элементов в u_arr должно быть равно n: {n}.")

    for value in arr:
        if not (abs(value) <= 10**9):
            raise ValueError(
                "Значение u_arr[i] находится вне допустимого диапазона: -10^9 ≤ u_arr[i] ≤ 10^9")

    result = randomized_quick_sort(arr, 0, len(arr) - 1)
    write_array_to_file(output_file_path, result)


def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task1'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    measure_performance(process_file, input_file_path, output_file_path)


if __name__ == "__main__":
    main()
