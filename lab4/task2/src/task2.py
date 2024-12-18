import sys
import os
from collections import deque

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import read_integers_from_file, write_array_to_file, measure_performance

def process_queue_operations(input_file_path, output_file_path):
    data = read_integers_from_file(input_file_path)
    M = int(data[0]) 
    commands = data[1:]  
    queue = deque()  
    result = []  
    
    for command in commands:
        if command.startswith('+'):
            parts = command.split()
            if len(parts) == 2:
                N = parts[1]
                queue.append(int(N))
        elif command == '-':
            if queue:  
                result.append(str(queue.popleft()))
    
    
    write_array_to_file(output_file_path, result)


def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task2'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    
    measure_performance(process_queue_operations, input_file_path, output_file_path)


if __name__ == "__main__":
    main()


