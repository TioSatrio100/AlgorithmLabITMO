import unittest
import os
from task8.src.task8 import process_file

class TestProcessFile(unittest.TestCase):

    def setUp(self):
        self.input_file_path = 'test_input.txt'
        self.output_file_path = 'test_output.txt'
        
        with open(self.input_file_path, 'w') as f:
            f.write("7\n3 1 4 2 2 3 4\n")  # Contoh input

    def tearDown(self):
        if os.path.exists(self.input_file_path):
            os.remove(self.input_file_path)
        if os.path.exists(self.output_file_path):
            os.remove(self.output_file_path)

    def test_process_file(self):
        process_file(self.input_file_path, self.output_file_path)
        
        with open(self.output_file_path, 'r') as f:
            output_data = f.read().strip() 

        expected_output = (
            "Swap elements at indices 1 and 2. "
            "Swap elements at indices 3 and 4. "
            "Swap elements at indices 4 and 5. "
            "Swap elements at indices 5 and 6. "
            "Swap elements at indices 2 and 3. "
            "Swap elements at indices 3 and 4."
        )
        
        self.assertEqual(output_data, expected_output.strip())  

if __name__ == '__main__':
    unittest.main()
