import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import measure_performance

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self, max_size=100):
        self.front = None
        self.rear = None
        self.size = 0
        self.max_size = max_size

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size >= self.max_size

    def Enqueue(self, data):
        if self.isFull():
            return "Queue is full"
        
        new_node = Node(data)
        
        if self.rear is None:  # If the queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1

    def Dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        
        dequeued_data = self.front.data
        self.front = self.front.next
        if self.front is None:  # If the queue becomes empty after dequeuing
            self.rear = None
        self.size -= 1
        return dequeued_data

    def print_queue(self):
        if self.isEmpty():
            return "Queue is empty"
        
        current = self.front
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)


def process_queue_operations(input_file_path, output_file_path):
    queue = Queue()
    with open(input_file_path, 'r') as file:
        operations = file.readlines()

    result = []
    
    for operation in operations:
        operation = operation.strip()  # Menghapus spasi di awal dan akhir
        if not operation:  # Skip baris kosong
            continue
        
        parts = operation.split()
        
        if not parts:  # Jika parts kosong, lanjutkan ke baris berikutnya
            continue
        
        command = parts[0]
        
        if command == "enqueue":
            value = int(parts[1])
            queue.Enqueue(value)
        elif command == "dequeue":
            dequeued_value = queue.Dequeue()
            result.append(str(dequeued_value))
        elif command == "print":
            result.append(queue.print_queue())
    
    with open(output_file_path, 'w') as file:
        file.write("\n".join(result))


def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task13_2'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    
    measure_performance(process_queue_operations, input_file_path, output_file_path)

if __name__ == "__main__":
    main()
