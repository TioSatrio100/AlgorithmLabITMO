import os
import sys


base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import read_problem_input3, write_output_file3, measure_performance

def process_file(input_file_path, output_file_path):
    N, X, A, B, AC, BC, AD, BD = read_problem_input3(input_file_path)
    table = set()
    
    for _ in range(N):
        if X in table:
            A = (A + AC) % 103
            B = (B + BC) % 1015
        else:
            table.add(X)
            A = (A + AD) % 103
            B = (B + BD) % 1015
        
        X = (X * A + B) % 1015
    
    write_output_file3(output_file_path, X, A, B)

def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task8'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    measure_performance(process_file, input_file_path, output_file_path)

if __name__ == "__main__":
    main()

