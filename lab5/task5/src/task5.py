import os
import sys
import heapq

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import read_problem_input, write_output_file2, measure_performance

def process_file(input_file_path, output_file_path):
    n, m, task_times = read_problem_input(input_file_path)

    thread_heap = [(0, i) for i in range(n)]
    heapq.heapify(thread_heap)

    results = []
    for task_time in task_times:
        finish_time, thread_index = heapq.heappop(thread_heap)
        results.append((thread_index, finish_time))
        heapq.heappush(thread_heap, (finish_time + task_time, thread_index))

    write_output_file2(output_file_path, results)

def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task5'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    measure_performance(process_file, input_file_path, output_file_path)

if __name__ == "__main__":
    main()

