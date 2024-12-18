import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import read_lines_from_file, write_array_to_file, measure_performance


def calculate_h_index(citations):
    citations.sort(reverse=True)
    h_index = 0
    for i, citation in enumerate(citations):
        if citation >= i + 1:
            h_index = i + 1
        else:
            break
    return h_index


def process_file(input_file_path, output_file_path):
    lines = read_lines_from_file(input_file_path)
    citations = list(map(int, lines[0].replace(',', ' ').split()))
    h_index = calculate_h_index(citations)
    write_array_to_file(output_file_path, [h_index])



def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task5'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    measure_performance(process_file, input_file_path, output_file_path)


if __name__ == "__main__":
    main()
