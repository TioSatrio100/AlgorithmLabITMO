import os

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def main():
   
    base_dir = 'lab'
    
   
    input_file_path = os.path.join(base_dir, 'task2', 'input.txt')
    output_file_path = os.path.join(base_dir, 'task2', 'output.txt')
    
    
   
    with open(input_file_path, 'r') as file:
        n = int(file.read().strip())
    
    
    result = fibonacci_iterative(n)
    
    
    with open(output_file_path, 'w') as file:
        file.write(f"{result}\n")

if __name__ == "__main__":
    main()