import sys
import os
import re

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import read_strings_from_file, write_output_to_file2, measure_performance

def is_match(pattern, string):
    regex = re.compile('^' + pattern.replace('?', '.').replace('*', '.*') + '$')
    return regex.match(string) is not None

def process_file(input_file_path, output_file_path):
    pattern, string = read_strings_from_file(input_file_path)
    result = "YES" if is_match(pattern, string) else "NO"
    write_output_to_file2(output_file_path, result)

def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task7'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    measure_performance(process_file, input_file_path, output_file_path)

if __name__ == "__main__":
    main()


