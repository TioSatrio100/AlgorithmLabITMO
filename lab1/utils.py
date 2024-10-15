import os
import time
import tracemalloc


def is_file_exists(file_path):
    """Check if a file exists, raise an error if not found."""
    if os.path.isfile(file_path):
        return True
    else:
        raise FileNotFoundError(f"Ошибка: Файл '{file_path}' не найден.")


def read_integers_from_file(file_path):
    
    with open(file_path, 'r') as file:
        n = int(file.readline().strip())
        u_arr = list(map(int, file.readline().strip().split()))
        return n, u_arr

def write_array_to_file(file_path, arr):
    with open(file_path, 'w') as file:
        file.write(" ".join(map(str, arr)) + "\n")

    
def read_integers_from_file2(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        arr = list(map(int, lines[0].strip().split()))
        target = int(lines[1].strip())
    return arr, target


def write_sorted_data_to_file(file_path, indices, sorted_arr):
    
    with open(file_path, 'w') as file:
        file.write(' '.join(map(str, [index + 1 for index in indices])) + '\n')
        file.write(' '.join(map(str, sorted_arr)) + '\n')

def write_sorted_data_to_file2(file_path, sorted_arr):
    
   with open(file_path, 'w') as file:
        file.write(" ".join(map(str, sorted_arr)) + "\n")


def write_swaps_to_file(file_path, swaps):
    with open(file_path, 'w') as file:
        for swap in swaps:
            file.write(swap + "\n")
        file.write("No more swaps needed.\n")


def read_binary_strings_from_file(file_path):
    with open(file_path, 'r') as file:
        line = file.readline().strip()
        return line.split()

def write_binary_result_to_file(file_path, C):
    with open(file_path, 'w') as file:
        file.write(''.join(map(str, C)) + '\n')

def write_search_results_to_file(file_path, indices):
    with open(file_path, 'w', encoding='utf-8') as file:
        if indices:
            file.write(f"{indices[0]}\n")
            file.write(f"Количество вхождений: {len(indices)}, Индексы: {', '.join(map(str, indices))}\n")
        else:
            file.write("-1\n")

def measure_performance(func, *args):
    
    start_time = time.perf_counter()
    tracemalloc.start()
    start_snapshot = tracemalloc.take_snapshot()

    result = func(*args)

    end_time = time.perf_counter()
    end_snapshot = tracemalloc.take_snapshot()
    tracemalloc.stop()

    top_stats = end_snapshot.compare_to(start_snapshot, 'lineno')
    total_memory_usage = sum(stat.size for stat in top_stats)

    print(f"Время выполнения: {end_time - start_time:.6f} секунд")
    print(f"Общее использование памяти: {total_memory_usage} байт")
    
    return result
