import os
import time
import tracemalloc

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
    start_time = time.perf_counter()
    
    tracemalloc.start()
    
    start_snapshot = tracemalloc.take_snapshot()
    
    base_dir = 'lab'
    input_file_path = os.path.join(base_dir, 'task4', 'input2.txt')
    output_file_path = os.path.join(base_dir, 'task4', 'output2.txt')
    
    # Validate input format
    with open(input_file_path, 'r') as file:
        try:
            n = int(file.read().strip())
            if n < 0 or n > 10**7:
                raise ValueError("Input is out of the valid range: 0 ≤ n ≤ 10^7")
        except ValueError as ve:
            print(f"Ошибка: {ve}")
            return
    
    result = last_digit_of_fibonacci(n)
    
    with open(output_file_path, 'w') as file:
        file.write(f"{result}\n")
    
    end_time = time.perf_counter()
    
    end_snapshot = tracemalloc.take_snapshot()
    
    tracemalloc.stop()
    
    top_stats = end_snapshot.compare_to(start_snapshot, 'lineno')
    total_memory_usage = sum(stat.size for stat in top_stats)
    
    print(f"Время выполнения: {end_time - start_time:.6f} секунд")
    print(f"Общее использование памяти: {total_memory_usage} байт")

if __name__ == "__main__":
    main()
