import unittest
import time
import tracemalloc
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task13_1 import process_stack_operations

class TestStackOperations(unittest.TestCase):

    def setUp(self):
        self.input_file_path = 'test_input.txt'
        self.output_file_path = 'test_output.txt'

    def tearDown(self):
        if os.path.exists(self.input_file_path):
            os.remove(self.input_file_path)
        if os.path.exists(self.output_file_path):
            os.remove(self.output_file_path)

    def test_basic_push_and_pop(self):
        input_data = "push 10\npush 20\npop\nprint"
        expected_output = "20\n10 -> None"

        with open(self.input_file_path, 'w') as f:
            f.write(input_data)

        process_stack_operations(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_pop_on_empty_stack(self):
        input_data = "pop\nprint"
        expected_output = "Stack is empty."

        with open(self.input_file_path, 'w') as f:
            f.write(input_data)

        process_stack_operations(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_multiple_push_and_print(self):
        input_data = "push 5\npush 15\npush 25\nprint"
        expected_output = "25 -> 15 -> 5 -> None"

        with open(self.input_file_path, 'w') as f:
            f.write(input_data)

        process_stack_operations(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_push_pop_sequence(self):
        input_data = "push 1\npush 2\npush 3\npop\npop\nprint"
        expected_output = "3\n2\n1 -> None"

        with open(self.input_file_path, 'w') as f:
            f.write(input_data)

        process_stack_operations(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, expected_output)

    def test_performance(self):
        large_input = "\n".join([f"push {i}" for i in range(10000)]) + "\nprint"

        with open(self.input_file_path, 'w') as f:
            f.write(large_input)

        start_time = time.time()
        process_stack_operations(self.input_file_path, self.output_file_path)
        end_time = time.time()

        execution_time = end_time - start_time

        tracemalloc.start()
        process_stack_operations(self.input_file_path, self.output_file_path)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertTrue(output_data.endswith("0 -> None"))
        print(f"Execution Time: {execution_time} seconds")
        print(f"Peak Memory Usage: {peak / 10**6} MB")

        self.assertLess(execution_time, 5)
        self.assertLess(peak / 10**6, 50)

if __name__ == '__main__':
    unittest.main()
