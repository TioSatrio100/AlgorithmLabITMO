import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import read_integers_from_file, write_array_to_file, measure_performance

def is_min_heap(arr, n):
    for i in range(n // 2):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    return True

def process_file(input_file_path, output_file_path):
    n, arr = read_integers_from_file(input_file_path)

    if not (1 <= n <= 10**6):
        raise ValueError("n is out of bounds: 1 <= n <= 10^6")

    for value in arr:
        if not (abs(value) <= 2 * 10**9):
            raise ValueError("Array values are out of bounds: |value| <= 2 * 10^9")

    result = "YES" if is_min_heap(arr, n) else "NO"
    write_array_to_file(output_file_path, [result])

def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task1'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    measure_performance(process_file, input_file_path, output_file_path)

if __name__ == "__main__":
    main()


