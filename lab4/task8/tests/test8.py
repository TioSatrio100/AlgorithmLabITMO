import unittest
import time
import tracemalloc
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task8 import process_file

class TestPostfixEvaluation(unittest.TestCase):

    def setUp(self):
        self.input_file_path = 'test_input.txt'
        self.output_file_path = 'test_output.txt'

    def tearDown(self):
        if os.path.exists(self.input_file_path):
            os.remove(self.input_file_path)
        if os.path.exists(self.output_file_path):
            os.remove(self.output_file_path)

    def test_simple_expression(self):
        input_data = "1\n2 3 +"
        expected_output = "5"
        
        with open(self.input_file_path, 'w') as f:
            f.write(input_data)
        
        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_multiple_operations(self):
        input_data = "1\n5 1 2 + 4 * + 3 -"
        expected_output = "14"

        with open(self.input_file_path, 'w') as f:
            f.write(input_data)
        
        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_large_numbers(self):
        input_data = "1\n10000 20000 +"
        expected_output = "30000"

        with open(self.input_file_path, 'w') as f:
            f.write(input_data)
        
        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_single_number(self):
        input_data = "1\n42"
        expected_output = "42"

        with open(self.input_file_path, 'w') as f:
            f.write(input_data)
        
        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_performance(self):
        large_expression = " ".join(str(i) for i in range(1, 10001)) + " + " * 9999
        input_data = f"1\n{large_expression}"
        
        with open(self.input_file_path, 'w') as f:
            f.write(input_data)
        
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
