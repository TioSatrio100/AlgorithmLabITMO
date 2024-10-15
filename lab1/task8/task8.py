import os
import time
import tracemalloc

def bubble_sort_with_swaps(arr):
    swaps = []
    n = len(arr)
    sorted = False

    while not sorted:
        sorted = True
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps.append(f"Swap elements at indices {i + 1} and {i + 2}.")
                sorted = False

    return arr, swaps

def main():
    start_time = time.perf_counter()
    tracemalloc.start()
    start_snapshot = tracemalloc.take_snapshot()

    base_dir = 'lab1'
    input_file_path = os.path.join(base_dir, 'task8', 'input.txt')
    output_file_path = os.path.join(base_dir, 'task8', 'output.txt')
    
    with open(input_file_path, 'r') as file:
        n = int(file.readline())
        arr = list(map(int, file.readline().strip().split()))

    if not (3 <= n <= 5000):
        raise ValueError("Длина массива должна быть в пределах: 3 ≤ n ≤ 5000")
    
    result, swaps = bubble_sort_with_swaps(arr)

    with open(output_file_path, 'w') as file:
        for swap in swaps:
            file.write(swap + "\n")
        file.write("No more swaps needed.\n")  # Final message

    end_time = time.perf_counter()
    end_snapshot = tracemalloc.take_snapshot()
    tracemalloc.stop()

    top_stats = end_snapshot.compare_to(start_snapshot, 'lineno')
    total_memory_usage = sum(stat.size for stat in top_stats)

    print(f"Время выполнения: {end_time - start_time:.6f} секунд")
    print(f"Общее использование памяти: {total_memory_usage} байт")

if __name__ == "__main__":
    main()




