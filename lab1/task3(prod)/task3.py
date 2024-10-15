import os
import time
import tracemalloc

def insertion_sort_recursive(arr, n):
    
    if n <= 1:
        return arr

   
    insertion_sort_recursive(arr, n - 1)

   
    key = arr[n - 1]
    j = n - 2

    
    while j >= 0 and arr[j] > key: 
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key  

    return arr

def main():
    start_time = time.perf_counter()
    tracemalloc.start()
    start_snapshot = tracemalloc.take_snapshot()

    base_dir = 'lab1'
    input_file_path = os.path.join(base_dir, 'task3(prod)', 'input.txt')
    output_file_path = os.path.join(base_dir, 'task3(prod)', 'output.txt')

    if not os.path.isfile(input_file_path):
        print("Ошибка: Файл не найден.")
        return

    with open(input_file_path, 'r') as file:
        n = int(file.readline())
        arr = list(map(int, file.readline().split()))

  
    if not (1 <= n <= 1000):
        print("Ошибка: Значение n находится вне допустимого диапазона: 1 ≤ n ≤ 1000")
        return
    
    if len(arr) != n:
        print(f"Ошибка: Количество элементов в arr должно совпадать с n: {n}.")
        return
    
    for i in range(len(arr)):
        if not (abs(arr[i]) <= 10**9):
            print("Ошибка: Значение arr[i] находится вне допустимого диапазона: -10^9 ≤ arr[i] ≤ 10^9")
            return
    
    result = insertion_sort_recursive(arr, n)

    with open(output_file_path, 'w') as file:
        file.write(" ".join(map(str, result)) + "\n")  

    end_time = time.perf_counter()
    end_snapshot = tracemalloc.take_snapshot()
    tracemalloc.stop()

    top_stats = end_snapshot.compare_to(start_snapshot, 'lineno')
    total_memory_usage = sum(stat.size for stat in top_stats)

    print(f"Время выполнения: {end_time - start_time:.6f} секунд")
    print(f"Общее использование памяти: {total_memory_usage} байт")

if __name__ == "__main__":
    main()


