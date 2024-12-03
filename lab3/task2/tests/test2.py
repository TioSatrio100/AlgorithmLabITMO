from task2 import process_file
import unittest
import time
import tracemalloc
import os
import sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


class TestProcessFile(unittest.TestCase):

    def setUp(self):
        self.input_file_path = 'test_input.txt'
        self.output_file_path = 'test_output.txt'

        with open(self.input_file_path, 'w') as f:
            f.write("3")

    def tearDown(self):
        if os.path.exists(self.input_file_path):
            os.remove(self.input_file_path)
        if os.path.exists(self.output_file_path):
            os.remove(self.output_file_path)

    def test_process_file(self):
        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, "1 3 2 ")

    def test_performance_process_file(self):
        large_input = "1000\n" + " ".join(str(i) for i in range(1000, 0, -1))
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