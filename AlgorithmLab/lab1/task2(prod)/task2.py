import os
import time
import tracemalloc

def insertion_sort_with_indices(arr):
    n = len(arr)
    indices = list(range(n))
    sorted_arr = arr[:]
    
    for i in range(1, n):
        key = sorted_arr[i]
        key_index = indices[i]
        j = i - 1
        
        while j >= 0 and key < sorted_arr[j]:
            sorted_arr[j + 1] = sorted_arr[j]
            indices[j + 1] = indices[j]
            j -= 1
            
        sorted_arr[j + 1] = key
        indices[j + 1] = key_index
    
    return indices, sorted_arr

def main():
    start_time = time.perf_counter()
    tracemalloc.start()
    start_snapshot = tracemalloc.take_snapshot()

    base_dir = 'lab1'
    input_file_path = os.path.join(base_dir, 'task2(prod)', 'input.txt')
    output_file_path = os.path.join(base_dir, 'task2(prod)', 'output.txt')

    file_exists = os.path.isfile(input_file_path)
    if not file_exists:
        print("Ошибка: Файл не найден.")
        return

    with open(input_file_path, 'r') as file:
        n = int(file.readline().strip())
        u_arr = list(map(int, file.readline().strip().split()))
    
    if 1 <= n <= 10**3 and len(u_arr) == n:
        if all(abs(value) <= 10**9 for value in u_arr):
            result_indices, sorted_arr = insertion_sort_with_indices(u_arr)
            with open(output_file_path, 'w') as file:
                file.write(' '.join(map(str, [index + 1 for index in result_indices])) + '\n')
                file.write(' '.join(map(str, sorted_arr)) + '\n')
        else:
            print("Ошибка: Значения u_arr[i] находятся вне допустимого диапазона: -10^9 ≤ u_arr[i] ≤ 10^9.")
    else:
        print("Ошибка: Значение n должно быть в диапазоне 1 ≤ n ≤ 1000 и количество элементов должно совпадать с n.")

    end_time = time.perf_counter()
    end_snapshot = tracemalloc.take_snapshot()
    tracemalloc.stop()

    top_stats = end_snapshot.compare_to(start_snapshot, 'lineno')
    total_memory_usage = sum(stat.size for stat in top_stats)

    print(f"Время выполнения: {end_time - start_time:.6f} секунд")
    print(f"Общее использование памяти: {total_memory_usage} байт")

if __name__ == "__main__":
    main()

