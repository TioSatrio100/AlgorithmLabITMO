import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import read_integers_from_file, write_array_to_file, measure_performance

def check_parentheses_balance(input_string):
    stack = [] 
    matching_parentheses = {')': '(', ']': '[', '}': '{'}  
    
    for i, char in enumerate(input_string):
        if char in '({[':
            
            stack.append((char, i + 1))  
        elif char in ')}]':
           
            if stack and stack[-1][0] == matching_parentheses[char]:
                
                stack.pop()
            else:
                
                return i + 1  
    
    
    if stack:
        return stack[0][1]  
    
   
    return "Success"

def process_file(input_file_path, output_file_path):
    
    input_string = read_integers_from_file(input_file_path)[0]
    
   
    result = check_parentheses_balance(input_string)
    
    
    write_array_to_file(output_file_path, [str(result)])

def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task4'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    
    measure_performance(process_file, input_file_path, output_file_path)

if __name__ == "__main__":
    main()

