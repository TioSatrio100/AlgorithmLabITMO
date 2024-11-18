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