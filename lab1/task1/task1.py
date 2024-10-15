import os
import time
import tracemalloc

def insertion_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

def main():
    # Start tracking time and memory
    start_time = time.perf_counter()
    tracemalloc.start()
    start_snapshot = tracemalloc.take_snapshot()

    base_dir = 'lab1'
    input_file_path = os.path.join(base_dir, 'task1', 'input.txt')
    output_file_path = os.path.join(base_dir, 'task1', 'output.txt')
    
    try:
        with open(input_file_path, 'r') as file:
            n = int(file.readline().strip())
            u_arr = list(map(int, file.readline().strip().split()))
        
        # Validate n and u_arr
        if not (1 <= n <= 10**3):
            raise ValueError("Значение n находится вне допустимого диапазона: 1 ≤ n ≤ 1000")
        
        if len(u_arr) != n:
            raise ValueError(f"Количество элементов в u_arr должно быть равно n: {n}.")
        
        for value in u_arr:
            if not (abs(value) <= 10**9):
                raise ValueError("Значение u_arr[i] находится вне допустимого диапазона: -10^9 ≤ u_arr[i] ≤ 10^9")
    
    except (FileNotFoundError, ValueError) as e:
        print(f"Ошибка: {e}")
        return
    
    result = insertion_sort(u_arr)
    
    try:
        with open(output_file_path, 'w') as file:
            file.write(f"{result}\n")
    except IOError as e:
        print(f"Ошибка при записи в файл: {e}")
        return

    # Stop tracking time and memory
    end_time = time.perf_counter()
    end_snapshot = tracemalloc.take_snapshot()
    tracemalloc.stop()

    # Calculate memory usage
    top_stats = end_snapshot.compare_to(start_snapshot, 'lineno')
    total_memory_usage = sum(stat.size for stat in top_stats)

    # Output execution time and memory usage
    print(f"Время выполнения: {end_time - start_time:.6f} секунд")
    print(f"Общее использование памяти: {total_memory_usage} байт")

if __name__ == "__main__":
    main()
