import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import read_special_case_10, write_array_to_file, measure_performance

def calculate_exit_times(n, customers):
    current_time = 0
    queue = []
    result = []
    
    for arrival_time, impatience in customers:
        queue_size = len(queue)
        
        if queue_size > impatience:
            result.append(arrival_time)
            continue
        
        exit_time = arrival_time + 10
        queue.append(exit_time)
        
        while queue and queue[0] <= arrival_time:
            queue.pop(0)
        
        result.append(exit_time)
    
    return result

def process_file(input_file_path, output_file_path):
    data = read_special_case_10(input_file_path)
    n = int(data[0])
    
    customers = []
    for i in range(n):
        hours, minutes, impatience = data[3*i + 1], data[3*i + 2], data[3*i + 3]
        arrival_time = hours * 60 + minutes
        customers.append((arrival_time, impatience))
    
    exit_times = calculate_exit_times(n, customers)
    
    result = []
    for time in exit_times:
        hours = time // 60
        minutes = time % 60
        result.append(f"{hours} {minutes}")
    
    write_array_to_file(output_file_path, result)

def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task10'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input1.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output1.txt')
    
    measure_performance(process_file, input_file_path, output_file_path)

if __name__ == "__main__":
    main()




