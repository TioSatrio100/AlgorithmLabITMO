
import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(base_dir)

from utils import is_file_exists, read_file, write_array_to_file, measure_performance

def binary_addition(A, B):
    n = len(A)
    C = [0] * (n + 1)
    carry = 0

    for i in range(n - 1, -1, -1):
        total = A[i] + B[i] + carry
        C[i + 1] = total % 2
        carry = total // 2

    C[0] = carry
    return C

def process_file(input_file_path, output_file_path):
    if not is_file_exists(input_file_path):
        raise FileNotFoundError(f"Ошибка: Файл '{input_file_path}' не найден.")
    lines = read_file(input_file_path)

    if len(lines) < 1:
        raise ValueError("Ошибка: Ожидалось как минимум одна строка в файле.")
    binary_values = lines[0].split()
    
    if len(binary_values) != 2:
        raise ValueError("Ошибка: Ожидалось два двоичных числа, разделенных пробелом.")
    A_str, B_str = binary_values
    n = len(A_str)

    if n < 1 or n > 1000:
        raise ValueError("Длина двоичного числа должна быть в диапазоне: 1 ≤ n ≤ 1000")
    A = list(map(int, A_str))
    B = list(map(int, B_str))
    C = binary_addition(A, B)
    write_array_to_file(output_file_path, C)

def main():
    base_dir = 'task9(prod)'
    input_file_path = os.path.join(base_dir,  'input.txt')
    output_file_path = os.path.join(base_dir,  'output.txt')
    measure_performance(process_file, input_file_path, output_file_path)

if __name__ == "__main__":
    main()

