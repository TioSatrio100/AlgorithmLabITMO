import os
import time
import tracemalloc

# Universal file reader that returns the content as a list of strings
def read_file(input_file):
    with open(input_file, 'r') as file:
        lines = file.read().strip().split("\n")
        n = int(lines[0])
        operations = []
        for line in lines[1:]:
            parts = line.split()
            if len(parts) == 2:
                operations.append((parts[0], parts[1]))
            elif len(parts) == 3:
                operations.append((parts[0], parts[1], parts[2]))
    return n, operations


def read_problem_input4(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

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
def read_problem_input(input_file_path):
    with open(input_file_path, 'r') as file:
        lines = file.readlines()
    data = []
    for line in lines:
        parts = line.split()  
        if len(parts) == 2:
            candidate = parts[0]
            try:
                vote_count = int(parts[1])
                data.append((candidate, vote_count))
            except ValueError:
                continue  
    return data

# Write output results to a file
def write_output_file(output_file, results):
    with open(output_file, 'w') as file:
        for result in results:
            file.write(str(result) + "\n")


def read_operations_from_file(input_file_path):
    operations = []
    with open(input_file_path, 'r') as file:
        n = int(file.readline().strip())  
        for _ in range(n):
            line = file.readline().strip().split()
            operations.append((line[0], int(line[1])))  
    return n, operations


def read_problem_input2(input_file_path):
    with open(input_file_path, 'r') as file:
        lines = file.readlines()
    data = []
    for line in lines:
        stripped_line = line.strip()  
        if stripped_line:  
            if stripped_line.isdigit():  
                data.append(int(stripped_line))
    return data


def write_output_file2(file_path, results):

    with open(file_path, 'w') as file:
        for thread_index, start_time in results:
            file.write(f"{thread_index} {start_time}\n")

def read_problem_input3(input_file_path):
    with open(input_file_path, 'r') as file:
        N, X, A, B = map(int, file.readline().split())
        AC, BC, AD, BD = map(int, file.readline().split())
    return N, X, A, B, AC, BC, AD, BD

def write_output_file3(output_file_path, X, A, B):
    with open(output_file_path, 'w') as file:
        file.write(f"{X} {A} {B}\n")


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