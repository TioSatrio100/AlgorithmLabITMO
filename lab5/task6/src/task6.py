import sys
import os
import heapq

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import read_special, write_output_file, measure_performance

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.index = 0
        self.entries = {}

    def add(self, x):
        heapq.heappush(self.heap, (x, self.index))
        self.entries[self.index] = x
        self.index += 1

    def extract_min(self):
        if self.heap:
            value, _ = heapq.heappop(self.heap)
            return value
        return '*'

    def decrease(self, x, y):
        index = x - 1
        new_value = y
        self.entries[index] = new_value
        self.heap = [(val, idx) if idx != index else (new_value, idx) for val, idx in self.heap]
        heapq.heapify(self.heap)

def process_file(input_file_path, output_file_path):
    queue = PriorityQueue()
    results = []

    lines = read_special(input_file_path)
    n = int(lines[0])

    for line in lines[1:]:
        parts = line.split()

        if parts[0] == 'A':
            queue.add(int(parts[1]))
        elif parts[0] == 'X':
            results.append(str(queue.extract_min()))
        elif parts[0] == 'D':
            queue.decrease(int(parts[1]), int(parts[2]))

    write_output_file(output_file_path, results)

def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task6'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    measure_performance(process_file, input_file_path, output_file_path)

if __name__ == "__main__":
    main()



