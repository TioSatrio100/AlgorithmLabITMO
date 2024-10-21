
import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(base_dir)


from utils import is_file_exists, read_integers_from_file, write_to_file, measure_performance

def bubble_sort_with_swaps(arr):
    swaps = []
    n = len(arr)
    sorted = False

    while not sorted:
        sorted = True
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps.append(f"Swap elements at indices {i + 1} and {i + 2}.")
                sorted = False

    return arr, swaps

def process_file(input_file_path, output_file_path):
    is_file_exists(input_file_path)
    n, arr = read_integers_from_file(input_file_path)
    
    if not (3 <= n <= 5000):
        raise ValueError("Длина массива должна быть в пределах: 3 ≤ n ≤ 5000")
    
    result, swaps = bubble_sort_with_swaps(arr)
    write_to_file(output_file_path, swaps)

def main():
    base_dir = 'task8'
    input_file_path = os.path.join(base_dir,  'input.txt')
    output_file_path = os.path.join(base_dir, 'output.txt')
    measure_performance(process_file, input_file_path, output_file_path)

if __name__ == "__main__":
    main()





