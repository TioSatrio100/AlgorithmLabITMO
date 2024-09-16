import os

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
    base_dir = 'lab'
    input_file_path = os.path.join(base_dir, 'task3', 'input.txt')
    output_file_path = os.path.join(base_dir, 'task3', 'output.txt')
    
    with open(input_file_path, 'r') as file:
        n = int(file.read().strip())
    
    if not (0 <= n <= 10**7):
        raise ValueError("Значение n находится вне допустимого диапазона: 0 ≤ n ≤ 10^7")
    
    result = last_digit_of_fibonacci(n)
    
    with open(output_file_path, 'w') as file:
        file.write(f"{result}\n")

if __name__ == "__main__":
    main()
