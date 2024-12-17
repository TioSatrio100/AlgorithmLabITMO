import unittest
import time
import tracemalloc
import os
import sys
from io import StringIO


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task2 import process_queue_operations

class TestQueueOperations(unittest.TestCase):

    def setUp(self):
        self.input_file_path = 'test_input.txt'
        self.output_file_path = 'test_output.txt'

    def tearDown(self):
        if os.path.exists(self.input_file_path):
            os.remove(self.input_file_path)
        if os.path.exists(self.output_file_path):
            os.remove(self.output_file_path)

    def test_basic_operations(self):
        input_data = "4\n+ 1\n+ 10\n- \n-"
        expected_output = "1\n10\n"
        
        with open(self.input_file_path, 'w') as f:
            f.write(input_data)
        
        process_queue_operations(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_operations_with_no_dequeue(self):
        input_data = "2\n+ 5\n+ 6"
        expected_output = ""
        
        with open(self.input_file_path, 'w') as f:
            f.write(input_data)
        
        process_queue_operations(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_operations_with_multiple_dequeues(self):
        input_data = "5\n+ 8\n+ 9\n- \n- \n-"
        expected_output = "8\n9\n"
        
        with open(self.input_file_path, 'w') as f:
            f.write(input_data)
        
        process_queue_operations(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_performance(self):
        large_input = "1000\n" + "\n".join(f"+ {i}" for i in range(1000)) + "\n" + "\n".join("-" for _ in range(1000))
        
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

        print(f"Execution Time: {execution_time} seconds")
        print(f"Peak Memory Usage: {peak / 10**6} MB")

        self.assertLess(execution_time, 5)  # Should complete within 5 seconds
        self.assertLess(peak / 10**6, 100)  # Should not exceed 100MB of memory

if __name__ == '__main__':
    unittest.main()

