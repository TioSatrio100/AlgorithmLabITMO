import unittest
import time
import tracemalloc
import os
import sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task4 import process_file 

class TestParenthesesBalance(unittest.TestCase):

    def setUp(self):
        self.input_file_path = 'test_input.txt'
        self.output_file_path = 'test_output.txt'

    def tearDown(self):
        if os.path.exists(self.input_file_path):
            os.remove(self.input_file_path)
        if os.path.exists(self.output_file_path):
            os.remove(self.output_file_path)

    def test_balanced_parentheses(self):
        input_data = "({[]})"
        expected_output = "Success"
        
        with open(self.input_file_path, 'w') as f:
            f.write(input_data)
        
        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_unbalanced_parentheses(self):
        input_data = "({[})"
        expected_output = "4"  # Error at position 4 (closing parenthesis)
        
        with open(self.input_file_path, 'w') as f:
            f.write(input_data)
        
        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_no_parentheses(self):
        input_data = "abcde"
        expected_output = "Success"
        
        with open(self.input_file_path, 'w') as f:
            f.write(input_data)
        
        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_empty_input(self):
        input_data = ""
        expected_output = "Success"
        
        with open(self.input_file_path, 'w') as f:
            f.write(input_data)
        
        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_multiple_errors(self):
        input_data = "({[}){"
        expected_output = "4" 
        
        with open(self.input_file_path, 'w') as f:
            f.write(input_data)
        
        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_performance(self):
        large_input = "{" + "{" * 50 + "}" * 50 + "}"  
        
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

        self.assertLess(execution_time, 5)  # Should complete within 5 seconds
        self.assertLess(peak / 10**6, 100)  # Should not exceed 100MB of memory

if __name__ == '__main__':
    unittest.main()
