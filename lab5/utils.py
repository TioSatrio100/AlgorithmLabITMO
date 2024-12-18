import os
import time
import tracemalloc

# Universal file reader that returns the content as a list of strings
def read_file(file_path):
    if not os.path.isfile(file_path):
        print(f"Ошибка: Файл '{file_path}' не найден.")
        return []
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Read integers from file
def read_integers_from_file(file_path):
    lines = read_file(file_path)
    if not lines:
        return 0, []
    try:
        n = int(lines[0])
        arr = list(map(int, lines[1].split()))
        return n, arr
    except (ValueError, IndexError) as e:
        print(f"Ошибка при разборе целых чисел из файла '{file_path}': {e}")
        return 0, []

# Write a list of integers to a file
def write_array_to_file(file_path, arr):
    with open(file_path, 'w') as file:
        file.write(" ".join(map(str, arr)) + "\n")

# Read input file (for specific format)
def read_problem_input(file_path):
    with open(file_path, 'r') as file:
        n, m = map(int, file.readline().split())
        task_times = list(map(int, file.readline().split()))
    return n, m, task_times

# Write output results to a file
def write_output_file(output_file, results):
    with open(output_file, 'w') as file:
        file.write(" ".join(map(str, results)) + "\n")


def read_special(input_file_path):
    with open(input_file_path, 'r') as file:
        lines = []
        for line in file:
            stripped_line = line.strip()
            if stripped_line:
                lines.append(stripped_line)
        return lines

def write_output_file2(file_path, results):

    with open(file_path, 'w') as file:
        for thread_index, start_time in results:
            file.write(f"{thread_index} {start_time}\n")

# Universal function for performance measurement
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