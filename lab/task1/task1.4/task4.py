import os

def main():
   
    base_dir = 'lab/task1'
    
   
    input_file_path = os.path.join(base_dir, 'task1.4', 'input.txt')
    output_file_path = os.path.join(base_dir, 'task1.4', 'output.txt')
    
  
    with open(input_file_path, 'r') as file:
        input_str = file.read().strip()
    
    
    a, b = map(int, input_str.split())
    
   
    if -10**9 <= a <= 10**9 and -10**9 <= b <= 10**9:
        result = a + b ** 2
    
    
    with open(output_file_path, 'w') as file:
        file.write(f"{result}\n")

if __name__ == "__main__":
    main()