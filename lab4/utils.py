import time
import tracemalloc



def read_lines_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]  
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error '{file_path}'. {e}")
        return []

def write_lines_to_file(file_path, lines):
    try:
        with open(file_path, 'w') as file:
            file.write("\n".join(lines) + "\n")
    except Exception as e:
        print(f"Error'{file_path}'. {e}")


def read_integers_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        return lines  

def write_array_to_file(file_path, result):
    with open(file_path, 'w') as file:
        file.write("\n".join(result) + "\n")


def read_special_case_10(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().split()
            return [int(x) for x in content]
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []
    except ValueError:
        print(f"File '{file_path}' cannot converse  to integer.")
        return []


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


