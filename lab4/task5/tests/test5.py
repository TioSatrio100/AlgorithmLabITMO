import unittest
import time
import tracemalloc
import os
import sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task5 import process_file, MaxStack  

class TestMaxStack(unittest.TestCase):

    def setUp(self):
        self.input_file_path = 'test_input.txt'
        self.output_file_path = 'test_output.txt'

    def tearDown(self):
        if os.path.exists(self.input_file_path):
            os.remove(self.input_file_path)
        if os.path.exists(self.output_file_path):
            os.remove(self.output_file_path)

    def test_basic_operations(self):
        input_data = "5\npush 2\npush 5\nmax\npop\nmax"
        expected_output = "5\n2\n"
        
        with open(self.input_file_path, 'w') as f:
            f.write(input_data)
        
        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_empty_stack_max(self):
        input_data = "2\nmax\npush 10\nmax"
        expected_output = "None\n10\n"
        
        with open(self.input_file_path, 'w') as f:
            f.write(input_data)
        
        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_multiple_push_and_pop(self):
        input_data = "6\npush 1\npush 2\npush 3\npop\nmax\npop"
        expected_output = "3\n2\n"
        
        with open(self.input_file_path, 'w') as f:
            f.write(input_data)
        
        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_max_after_pop(self):
        input_data = "4\npush 4\npush 10\npop\nmax"
        expected_output = "10\n"
        
        with open(self.input_file_path, 'w') as f:
            f.write(input_data)
        
        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_performance(self):
        large_input = "1000\n" + "\n".join(f"push {i}" for i in range(1, 1001)) + "\n" + "\n".join("max" for _ in range(1000)) + "\npop\n"
        
        with open(self.input_file_path, 'w') as f:
            f.write(large_input)
        
        start_time = time.time()
        process_file(self.input_file_path, self.output_file_path)
        end_time = time.time()

        execution_time = end_time - start_time

        tracemalloc.start()
        process_file(self.input_file_path, self.output_file_path)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"Execution Time: {execution_time} seconds")
        print(f"Peak Memory Usage: {peak / 10**6} MB")

        self.assertLess(execution_time, 5)  
        self.assertLess(peak / 10**6, 100)  

if __name__ == '__main__':
    unittest.main()
