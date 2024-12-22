import unittest
import time
import tracemalloc
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task6 import process_file

class TestTask6(unittest.TestCase):

    def setUp(self):
        self.input_file_path = 'test_input.txt'
        self.output_file_path = 'test_output.txt'

    def tearDown(self):
        if os.path.exists(self.input_file_path):
            os.remove(self.input_file_path)
        if os.path.exists(self.output_file_path):
            os.remove(self.output_file_path)

    def test_process_file_case1(self):
        with open(self.input_file_path, 'w') as f:
            f.write("6\n3 10 2 1 20 4\n")

        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        expected_output = "3\n3 10 20"
        self.assertEqual(output_data, expected_output)

    def test_process_file_case2(self):
        with open(self.input_file_path, 'w') as f:
            f.write("5\n10 20 10 30 40\n")

        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        expected_output = "4\n10 20 30 40"
        self.assertEqual(output_data, expected_output)

    def test_process_file_single_element(self):
        with open(self.input_file_path, 'w') as f:
            f.write("1\n7\n")

        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        expected_output = "1\n7"
        self.assertEqual(output_data, expected_output)

    def test_performance_process_file(self):
        large_input = "10000\n" + " ".join(str(i) for i in range(1, 10001)) + "\n"
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

        self.assertLess(execution_time, 10)
        self.assertLess(peak / 10**6, 100)

if __name__ == '__main__':
    unittest.main()

