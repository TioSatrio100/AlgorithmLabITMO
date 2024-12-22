import os
import sys

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import read_problem_input, write_output_file, measure_performance

def process_elections(data):
    votes = {}
    for candidate, vote_count in data:
        votes[candidate] = votes.get(candidate, 0) + int(vote_count)

    sorted_candidates = sorted(votes.items())
    res = [f"{candidate} {count}\n" for candidate, count in sorted_candidates]
    return res

def process_file(input_file_path, output_file_path):
    data = read_problem_input(input_file_path)
    
    results = process_elections(data)
    
    write_output_file(output_file_path, results)

def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task5'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    measure_performance(process_file, input_file_path, output_file_path)

if __name__ == "__main__":
    main()

