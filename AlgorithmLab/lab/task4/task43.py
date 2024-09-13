import os

import time

def last_digit_of_fibonacci(n):

    
    pisano_period = 60
    
   
    n_mod = n % pisano_period
    
    
    if n_mod == 0:
        return 0
    
    
    a, b = 0, 1
    
    for _ in range(n_mod - 1):
        a, b = b, (a + b) % 10
    
   
    return b

def main():
    
    start_time= time.perf_counter()
    
    base_dir = 'lab'
    
   
    input_file_path = os.path.join(base_dir, 'task4', 'input2.txt')
    output_file_path = os.path.join(base_dir, 'task4', 'output2.txt')
    
   
    with open(input_file_path, 'r') as file:
        n = int(file.read().strip())
    
   
    result = last_digit_of_fibonacci(n)
    
    
    with open(output_file_path, 'w') as file:
        file.write(f"{result}\n")

    end_time = time.perf_counter()
    print(f"excecution: {end_time - start_time:.6f} second")



if __name__ == "__main__":
    main()