import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import measure_performance, read_lines_from_file, write_lines_to_file

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            return None
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def print_stack(self):
        if self.isEmpty():
            return "Stack is empty."
        current = self.top
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result) + " -> None"

def process_stack_operations(input_file_path, output_file_path):
    stack = Stack()
    operations = read_lines_from_file(input_file_path) 
    
    result = []
    
    for operation in operations:
        parts = operation.split()
        command = parts[0]
        
        if command == "push":
            value = int(parts[1])
            stack.push(value)
        elif command == "pop":
            popped_value = stack.pop()
            if popped_value is not None:
                result.append(str(popped_value))
        elif command == "print":
            result.append(stack.print_stack())
    
    write_lines_to_file(output_file_path, result) 


def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task13_1'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    
    measure_performance(process_stack_operations, input_file_path, output_file_path)

if __name__ == "__main__":
    main()
