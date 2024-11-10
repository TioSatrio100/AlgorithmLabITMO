import unittest
import os
from task4.src.task4 import process_file

class TestProcessFile(unittest.TestCase):

    def setUp(self):
        
        self.input_file_path = 'test_input.txt'
        self.output_file_path = 'test_output.txt'
        
        
        with open(self.input_file_path, 'w') as f:
            f.write("5\n1 5 8 12 13\n5\n8 1 23 1 11\n")

    def tearDown(self):
        
        if os.path.exists(self.input_file_path):
            os.remove(self.input_file_path)
        if os.path.exists(self.output_file_path):
            os.remove(self.output_file_path)

    def test_process_file(self):
       
        process_file(self.input_file_path, self.output_file_path)
        
        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip()

        
        self.assertEqual(output_data, "2 0 -1 0 -1")

if __name__ == '__main__':
    unittest.main()