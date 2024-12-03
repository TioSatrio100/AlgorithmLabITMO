import unittest
import os
from task6.src.task6 import process_file

class TestProcessFile(unittest.TestCase):

    def setUp(self):
        
        self.input_file_path = 'test_input.txt'
        self.output_file_path = 'test_output.txt'
        
        
        with open(self.input_file_path, 'w') as f:
            f.write("date,price\n 2024-10-01,258.02 \n2024-10-02,249.02\n 2024-10-03,240.66\n 2024-10-04,250.08\n 2024-10-07,240.83\n2024-10-08,240.83\n 2024-10-09,241.05\n 2024-10-10,238.77\n 2024-10-11,217.80\n2024-10-14,219.16\n 2024-10-15,219.57")

    def tearDown(self):
        
        if os.path.exists(self.input_file_path):
            os.remove(self.input_file_path)
        if os.path.exists(self.output_file_path):
            os.remove(self.output_file_path)

    def test_process_file(self):
       
        process_file(self.input_file_path, self.output_file_path)
        
        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        
        self.assertEqual(output_data, "Компания: Tesla\n Период: 2024-10-01 до 2023-10-15\n Дата покупки: 2024-10-01\n Дата продажи: 2024-10-15\n Максимальная прибыль: 2615.79")

if __name__ == '__main__':
    unittest.main()


from task4 import process_file
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
            f.write("date,price\n 2024-10-01,258.02 \n2024-10-02,249.02\n 2024-10-03,240.66\n 2024-10-04,250.08\n 2024-10-07,240.83\n2024-10-08,240.83\n 2024-10-09,241.05\n 2024-10-10,238.77\n 2024-10-11,217.80\n2024-10-14,219.16\n 2024-10-15,219.57")

    def tearDown(self):
        if os.path.exists(self.input_file_path):
            os.remove(self.input_file_path)
        if os.path.exists(self.output_file_path):
            os.remove(self.output_file_path)

    def test_process_file(self):
        process_file(self.input_file_path, self.output_file_path)

        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        self.assertEqual(output_data, "Компания: Tesla\n Период: 2024-10-01 до 2023-10-15\n Дата покупки: 2024-10-01\n Дата продажи: 2024-10-15\n Максимальная прибыль: 2615.79")

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