import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import read_integers_from_file, write_array_to_file, measure_performance

class MaxStack:
    def __init__(self):
        self.data_stack = []
        self.max_stack = []
    
    def push(self, value):
        self.data_stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)
    
    def pop(self):
        if self.data_stack:
            value = self.data_stack.pop()
            if value == self.max_stack[-1]:
                self.max_stack.pop()
    
    def max(self):
        if self.max_stack:
            return self.max_stack[-1]
        return None

def process_file(input_file_path, output_file_path):
    commands = read_integers_from_file(input_file_path)
    n = int(commands[0])
    operations = commands[1:]
    
    stack = MaxStack()
    result = []
    
    idx = 0
    while idx < len(operations):
        command = operations[idx]
        
        if command.startswith("push"):
            _, V = command.split()
            stack.push(int(V))
        elif command == "pop":
            stack.pop()
        elif command == "max":
            result.append(str(stack.max()))
        
        idx += 1
    
    write_array_to_file(output_file_path, result)

def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task5'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    
    measure_performance(process_file, input_file_path, output_file_path)

if __name__ == "__main__":
    main()

