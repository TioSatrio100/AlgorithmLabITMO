import os
import time
import tracemalloc

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

def main():
    start_time = time.perf_counter()
    tracemalloc.start()
    start_snapshot = tracemalloc.take_snapshot()

    base_dir = 'lab1'
    input_file_path = os.path.join(base_dir, 'task9(prod)', 'input.txt')
    output_file_path = os.path.join(base_dir, 'task9(prod)', 'output.txt')

    with open(input_file_path, 'r') as file:
        line = file.readline().strip()
        A_str, B_str = line.split()

    n = len(A_str)
    
    if n < 1 or n > 1000:
        raise ValueError("Длина двоичного числа должна быть в диапазоне: 1 ≤ n ≤ 1000")

    A = list(map(int, A_str))
    B = list(map(int, B_str))

    C = binary_addition(A, B)

    with open(output_file_path, 'w') as file:
        file.write(''.join(map(str, C)) + '\n')

    end_time = time.perf_counter()
    end_snapshot = tracemalloc.take_snapshot()
    tracemalloc.stop()

    top_stats = end_snapshot.compare_to(start_snapshot, 'lineno')
    total_memory_usage = sum(stat.size for stat in top_stats)

    print(f"Время выполнения: {end_time - start_time:.6f} секунд")
    print(f"Использование памяти: {total_memory_usage} байт")

if __name__ == "__main__":
    main()
