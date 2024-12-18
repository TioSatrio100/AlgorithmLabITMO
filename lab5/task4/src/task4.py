import sys
import os
import random

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import read_file, write_output_file, measure_performance


def sift_down(i, size, arr, swaps):
    min_index = i
    left = 2 * i + 1  
    right = 2 * i + 2  

    if left < size and arr[left] < arr[min_index]:
        min_index = left

    if right < size and arr[right] < arr[min_index]:
        min_index = right

    if i != min_index:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swaps.append((i, min_index))  
        sift_down(min_index, size, arr, swaps)  


def build_min_heap(arr):
    size = len(arr)
    swaps = []

    for i in range(size // 2 - 1, -1, -1):
        sift_down(i, size, arr, swaps)
    return swaps


def process_file(input_file_path, output_file_path):
    lines = read_file(input_file_path)
    n = int(lines[0])
    arr = list(map(int, lines[1].split()))

    if not (1 <= n <= 10**5):
        raise ValueError("Значение n должно быть в диапазоне: 1 ≤ n ≤ 10^5")
    if len(arr) != n:
        raise ValueError(f"Количество элементов в массиве должно быть равно n: {n}")
    for value in arr:
        if not (0 <= value <= 10**9):
            raise ValueError("Значение массива должно быть в диапазоне: 0 ≤ ai ≤ 10^9")

    swaps = build_min_heap(arr)

    output_lines = [f"{len(swaps)}\n"] + [f"{i} {j}\n" for i, j in swaps]
    write_output_file(output_file_path, output_lines)


def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task4'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    measure_performance(process_file, input_file_path, output_file_path)


if __name__ == "__main__":
    main()
