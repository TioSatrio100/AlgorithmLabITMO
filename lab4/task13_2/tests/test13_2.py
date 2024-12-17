import unittest
import os
import sys
import time
import tracemalloc

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task13_2 import process_queue_operations

class TestQueueOperations(unittest.TestCase):
    def setUp(self):
        self.input_file_path = 'test_input.txt'
        self.output_file_path = 'test_output.txt'

    def tearDown(self):
        if os.path.exists(self.input_file_path):
            os.remove(self.input_file_path)
        if os.path.exists(self.output_file_path):
            os.remove(self.output_file_path)

    def test_basic_enqueue_and_dequeue(self):
        input_data = "enqueue 10\nenqueue 20\ndequeue\nprint"
        expected_output = "10\n20"

        with open(self.input_file_path, 'w') as f:
            f.write(input_data)

        process_queue_operations(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_dequeue_empty_queue(self):
        input_data = "dequeue\nprint"
        expected_output = "Queue is empty\nQueue is empty"

        with open(self.input_file_path, 'w') as f:
            f.write(input_data)

        process_queue_operations(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_enqueue_until_full(self):
        input_data = "\n".join([f"enqueue {i}" for i in range(101)]) + "\nprint"
        expected_output = "Queue is full\n" + " -> ".join(map(str, range(100)))

        with open(self.input_file_path, 'w') as f:
            f.write(input_data)

        process_queue_operations(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_multiple_enqueue_dequeue_sequence(self):
        input_data = "enqueue 5\nenqueue 10\ndequeue\nenqueue 15\nprint"
        expected_output = "5\n10 -> 15"

        with open(self.input_file_path, 'w') as f:
            f.write(input_data)

        process_queue_operations(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_performance_large_input(self):
        large_input = "\n".join([f"enqueue {i}" for i in range(10000)]) + "\nprint"

        with open(self.input_file_path, 'w') as f:
            f.write(large_input)

        start_time = time.time()
        process_queue_operations(self.input_file_path, self.output_file_path)
        end_time = time.time()

        execution_time = end_time - start_time

        tracemalloc.start()
        process_queue_operations(self.input_file_path, self.output_file_path)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertTrue(output_data.endswith("0 -> 1 -> 2 -> ... -> 9999"))
        print(f"Execution Time: {execution_time} seconds")
        print(f"Peak Memory Usage: {peak / 10**6} MB")

        self.assertLess(execution_time, 5)
        self.assertLess(peak / 10**6, 50)

if __name__ == '__main__':
    unittest.main()
