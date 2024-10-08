import os
import time
import tracemalloc

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def main():
    start_time = time.perf_counter()
    
    tracemalloc.start()
    
    start_snapshot = tracemalloc.take_snapshot()

    base_dir = 'lab'
    input_file_path = os.path.join(base_dir, 'task4', 'input.txt')
    output_file_path = os.path.join(base_dir, 'task4', 'output.txt')
    
    try:
        with open(input_file_path, 'r') as file:
            n = int(file.read().strip())
            
            if not (0 <= n <= 45):
                raise ValueError("Значение n должно быть в диапазоне 0 ≤ n ≤ 45.")
    
    except (FileNotFoundError, ValueError) as e:
        print(f"Ошибка: {e}")
        return
    
    result = fibonacci_iterative(n)
    
    try:
        with open(output_file_path, 'w') as file:
            file.write(f"{result}\n")
    except IOError as e:
        print(f"Ошибка при записи в файл: {e}")
        return
    
    end_time = time.perf_counter()
    
    end_snapshot = tracemalloc.take_snapshot()
    
    tracemalloc.stop()
    
    top_stats = end_snapshot.compare_to(start_snapshot, 'lineno')
    total_memory_usage = sum(stat.size for stat in top_stats)
    
    print(f"Время выполнения: {end_time - start_time:.6f} секунд")
    print(f"Общее использование памяти: {total_memory_usage} байт")

if __name__ == "__main__":
    main()
