import os
import time
import tracemalloc

# Universal file existence check, returns True or False
def is_file_exists(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        return False

# Universal file reader that returns the content as a list of strings
def read_file(file_path):
    if not is_file_exists(file_path):
        raise FileNotFoundError(f"Ошибка: Файл '{file_path}' не найден.")
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Universal file writer that writes a list of strings or numbers to file
def write_to_file(file_path, data):
    with open(file_path, 'w') as file:
        if isinstance(data, list):
            file.write("\n".join(map(str, data)) + "\n")
        else:
            file.write(str(data) + "\n")

# Read integers from file, but cope if the format changes
def read_integers_from_file(file_path):
    lines = read_file(file_path)
    n = int(lines[0])
    arr = list(map(int, lines[1].split()))  
    return n, arr

# Write a list of integers to a file
def write_array_to_file(file_path, arr):
    write_to_file(file_path, [" ".join(map(str, arr))])

# Universal func for performance measurement
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
