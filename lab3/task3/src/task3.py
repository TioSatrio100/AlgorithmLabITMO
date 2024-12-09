
import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import read_problem_input, write_output_file, measure_performance

def qsort(a, left, right):
    if left < right:
        pivot = a[(left + right) // 2]
        i = left
        j = right
        while i <= j:
            while a[i] < pivot:
                i += 1
            while a[j] > pivot:
                j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
        qsort(a, left, j)
        qsort(a, i, right)


def is_non_decreasing(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True


def process_file(input_file_path, output_file_path):
    n, m, sizes = read_problem_input(input_file_path)

    if len(sizes) != n:
        raise ValueError(
            f"Количество размеров ({len(sizes)}) не совпадает с n ({n})")

    qsort(sizes, 0, len(sizes) - 1)

    result = "ДА" if is_non_decreasing(sizes) else "НЕТ"
    write_output_file(output_file_path, result)


def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task3'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    measure_performance(process_file, input_file_path, output_file_path)


if __name__ == "__main__":
    main()
