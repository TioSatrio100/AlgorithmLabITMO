import os
import sys

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import read_problem_input4, write_array_to_file, measure_performance


def count_beautiful_pairs(n, k, stones, beautiful_pairs):
    beautiful_pairs_set = set(beautiful_pairs)
    last_indices = {}
    pair_count = 0

    for char in stones:
        for pair in beautiful_pairs_set:
            if len(pair) == 2:  
                if char == pair[1] and pair[0] in last_indices:
                    pair_count += last_indices[pair[0]]
        
        if char in last_indices:
            last_indices[char] += 1
        else:
            last_indices[char] = 1

    return pair_count



def process_file(input_file_path, output_file_path):
    data = read_problem_input4(input_file_path)
    n, k = map(int, data[0].strip().split())
    stones = data[1].strip()
    beautiful_pairs = [tuple(line.strip()) for line in data[2:]]
    result = count_beautiful_pairs(n, k, stones, beautiful_pairs)
    write_array_to_file(output_file_path, [f"{result}\n"])


def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task7'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    measure_performance(process_file, input_file_path, output_file_path)


if __name__ == "__main__":
    main()





