import unittest
import time
import tracemalloc
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task7 import process_file

class TestProcessFileTask7(unittest.TestCase):

    def setUp(self):
        self.input_file_path = 'test_input.txt'
        self.output_file_path = 'test_output.txt'

    def tearDown(self):
        if os.path.exists(self.input_file_path):
            os.remove(self.input_file_path)
        if os.path.exists(self.output_file_path):
            os.remove(self.output_file_path)

    def test_process_file_match(self):
        with open(self.input_file_path, 'w') as f:
            f.write("k?t*n\nkitten")

        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        expected_output = "YES"
        self.assertEqual(output_data, expected_output)

    def test_process_file_no_match(self):
        with open(self.input_file_path, 'w') as f:
            f.write("k?t?n\nkitten")

        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        expected_output = "NO"
        self.assertEqual(output_data, expected_output)

    def test_process_file_empty_pattern(self):
        with open(self.input_file_path, 'w') as f:
            f.write("\nkitten")

        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        expected_output = "NO"
        self.assertEqual(output_data, expected_output)

    def test_process_file_empty_string(self):
        with open(self.input_file_path, 'w') as f:
            f.write("k*t?n\n")

        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        expected_output = "NO"
        self.assertEqual(output_data, expected_output)

    def test_performance_process_file(self):
        large_pattern = "a*b*c*d*e*f*"
        large_string = "a" * 10000 + "b" * 10000 + "c" * 10000 + "d" * 10000 + "e" * 10000 + "f" * 10000

        with open(self.input_file_path, 'w') as f:
            f.write(f"{large_pattern}\n{large_string}")

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

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, "YES")
        self.assertLess(execution_time, 10)
        self.assertLess(peak / 10**6, 100)

if __name__ == '__main__':
    unittest.main()

