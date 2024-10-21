
import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(base_dir)

from utils import read_file, write_to_file, measure_performance

def linear_search(arr, target):
    indices = []
    for index in range(len(arr)):
        if arr[index] == target:
            indices.append(index + 1)  
    return indices

def process_file(input_file_path, output_file_path):

    arr, target = read_file(input_file_path)

    if not (0 <= len(arr) <= 10**3):
        raise ValueError("Длина массива выходит за пределы допустимого диапазона: 0 ≤ n ≤ 10^3")

    
    indices = linear_search(arr, target)

    
    write_to_file(output_file_path, indices)

def main():
    base_dir = 'task4'
    input_file_path = os.path.join(base_dir,  'input.txt')
    output_file_path = os.path.join(base_dir,  'output.txt')

    
    measure_performance(process_file, input_file_path, output_file_path)

if __name__ == "__main__":
    main()



