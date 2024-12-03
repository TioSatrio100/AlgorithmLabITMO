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
        first_line = file.readline().strip()
        n, m = map(int, first_line.split())
        sizes = list(map(int, file.readline().strip().split()))
    return n, m, sizes

# Write output results to a file
def write_output_file(output_file, results):
    with open(output_file, 'w') as file:
        file.write(" ".join(map(str, results)) + "\n")

# Read data from a input file for stock
def read_data(filename):
    dates = []
    prices = []
    lines = read_file(filename)
    for line in lines[1:]:  
        if line:  
            parts = line.split(',')
            if len(parts) == 2:  
                date, price = parts
                dates.append(date)
                prices.append(float(price))
            else:
                print(f"Предупреждение: Найдена и проигнорирована некорректная строка: {line}")
    return dates, prices

# Write formatted output to a file fro stock data
def write_output(filename, company_name, period, buy_date, sell_date, max_profit):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Компания: {company_name}\n")
        file.write(f"Период: {period}\n")
        file.write(f"Дата покупки: {buy_date}\n")
        file.write(f"Дата продажи: {sell_date}\n")
        file.write(f"Максимальная прибыль: {max_profit}\n")

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