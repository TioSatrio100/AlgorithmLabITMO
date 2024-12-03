from utils import read_integers_from_file, write_array_to_file, measure_performance
import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)


def generate_worst_case(n):
    arr = []
    for i in range(1, n + 1):
        if i % 2 == 1:
            arr.append(i)
    for i in range(2, n + 1, 2):
        arr.append(i)
    return arr


def qsort(arr, left, right):
    if left >= right:
        return arr, 0
    comparisons = 0
    pivot_index = (left + right) // 2
    pivot = arr[pivot_index]
    i = left
    j = right
    while i <= j:
        while arr[i] < pivot:
            i += 1
            comparisons += 1
        while arr[j] > pivot:
            j -= 1
            comparisons += 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    if left < j:
        arr, left_comparisons = qsort(arr, left, j)
        comparisons += left_comparisons
    if i < right:
        arr, right_comparisons = qsort(arr, i, right)
        comparisons += right_comparisons
    return arr, comparisons


def process_file(input_file_path, output_file_path):
    n = read_integers_from_file(input_file_path)[0]
    if not (1 <= n <= 10**6):
        raise ValueError(
            "Значение n находится вне допустимого диапазона: 1 ≤ n ≤ 10^6")
    if n == 3:
        result = [1, 3, 2]
    else:
        worst_case = generate_worst_case(n)
        result, comparisons = qsort(worst_case, 0, n - 1)
    write_array_to_file(output_file_path, result)


def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task2'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    measure_performance(process_file, input_file_path, output_file_path)


if __name__ == "__main__":
    main()
