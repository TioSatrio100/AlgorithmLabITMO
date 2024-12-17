import unittest
import time
import tracemalloc
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task10 import process_file

class TestCustomerQueue(unittest.TestCase):

    def setUp(self):
        self.input_file_path = 'test_input.txt'
        self.output_file_path = 'test_output.txt'

    def tearDown(self):
        if os.path.exists(self.input_file_path):
            os.remove(self.input_file_path)
        if os.path.exists(self.output_file_path):
            os.remove(self.output_file_path)

    def test_single_customer(self):
        input_data = "1\n10 0 0"
        expected_output = "10 10"

        with open(self.input_file_path, 'w') as f:
            f.write(input_data)
        
        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_multiple_customers_no_impatience(self):
        input_data = "2\n10 0 0\n10 10 0"
        expected_output = "10 10\n10 20"

        with open(self.input_file_path, 'w') as f:
            f.write(input_data)

        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_customer_leaves_due_to_impatience(self):
        input_data = "2\n10 0 0\n10 5 0"
        expected_output = "10 10\n10 5"

        with open(self.input_file_path, 'w') as f:
            f.write(input_data)
        
        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_impatience_with_large_queue(self):
        input_data = "3\n10 0 0\n10 5 0\n10 15 1"
        expected_output = "10 10\n10 5\n10 25"

        with open(self.input_file_path, 'w') as f:
            f.write(input_data)

        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_performance(self):
        large_input = "1000\n" + "\n".join(f"{10 + i // 60} {i % 60} {i % 3}" for i in range(1000))
        
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




