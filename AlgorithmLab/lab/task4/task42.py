import os

import time

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def main():
   
    start_time= time.perf_counter()

    base_dir = 'lab'
    
   
    input_file_path = os.path.join(base_dir, 'task4', 'input.txt')
    output_file_path = os.path.join(base_dir, 'task4', 'output.txt')
    
    
    with open(input_file_path, 'r') as file:
        n = int(file.read().strip())
    
    
    result = fibonacci_iterative(n)
    
   
    with open(output_file_path, 'w') as file:
        file.write(f"{result}\n")

    end_time = time.perf_counter()
    print(f"excecution: {end_time - start_time:.6f} second")

if __name__ == "__main__":
    main()