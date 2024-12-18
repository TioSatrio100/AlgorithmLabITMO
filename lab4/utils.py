import time
import tracemalloc

def read_integers_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        return lines  

def write_array_to_file(file_path, result):
    with open(file_path, 'w') as file:
        file.write("\n".join(result) + "\n")


def read_special_case_10(input_file_path):
    with open(input_file_path, 'r') as file:
        n = int(file.readline().strip()) 
        customers = []
        
        
        for _ in range(n):
            line = file.readline().strip().split()
            hour, minute, impatience = map(int, line)  
            customers.append((hour, minute, impatience)) 
        
    return n, customers


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


