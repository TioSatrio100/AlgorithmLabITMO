import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import read_integers_from_file, write_array_to_file, measure_performance

def evaluate_postfix(expression):
    stack = []
    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
    
    return stack.pop()

def process_file(input_file_path, output_file_path):
    data = read_integers_from_file(input_file_path)
    n = int(data[0])
    expression = data[1].split()
    
    result = evaluate_postfix(expression)
    
    write_array_to_file(output_file_path, [str(result)])

def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task8'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    
    measure_performance(process_file, input_file_path, output_file_path)

if __name__ == "__main__":
    main()

