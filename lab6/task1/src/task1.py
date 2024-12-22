import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import read_operations_from_file, write_output_file, measure_performance

def process_operations(input_file_path, output_file_path):
    n, operations = read_operations_from_file(input_file_path)

    data_set = set()
    results = []

    for op_type, x in operations:
        if op_type == 'A':  
            data_set.add(x)
        elif op_type == 'D':  
            data_set.discard(x)
        elif op_type == '?':  
            results.append('Y' if x in data_set else 'N')

    write_output_file(output_file_path, results)

def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task1'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    measure_performance(process_operations, input_file_path, output_file_path)

if __name__ == "__main__":
    main()




