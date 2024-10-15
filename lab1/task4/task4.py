import os
import time
import tracemalloc

def linear_search(arr, target):
    indices = []
    for index in range(len(arr)):
        if arr[index] == target:
            indices.append(index + 1)  # Indeks 1-based
    return indices

def main():
    start_time = time.perf_counter()
    tracemalloc.start()
    start_snapshot = tracemalloc.take_snapshot()

    base_dir = 'lab1'
    input_file_path = os.path.join(base_dir, 'task4', 'input.txt')
    output_file_path = os.path.join(base_dir, 'task4', 'output.txt')

    with open(input_file_path, 'r') as file:
        lines = file.readlines()
        arr = list(map(int, lines[0].strip().split()))
        target = int(lines[1].strip())

    if not (0 <= len(arr) <= 10**3):
        raise ValueError("Длина массива выходит за пределы допустимого диапазона: 0 ≤ n ≤ 10^3")

    indices = linear_search(arr, target)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        if indices:
            file.write(f"{indices[0]}\n")
            file.write(f"Количество вхождений: {len(indices)}, Индексы: {', '.join(map(str, indices))}\n")
        else:
            file.write("-1\n")

    end_time = time.perf_counter()
    end_snapshot = tracemalloc.take_snapshot()
    tracemalloc.stop()

    top_stats = end_snapshot.compare_to(start_snapshot, 'lineno')
    total_memory_usage = sum(stat.size for stat in top_stats)

    print(f"Время выполнения: {end_time - start_time:.6f} секунд")
    print(f"Общее использование памяти: {total_memory_usage} байт")

if __name__ == "__main__":
    main()


