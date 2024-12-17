
import sys
import os
from collections import deque

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import read_integers_from_file, write_array_to_file, measure_performance

def process_queue_operations(input_file_path, output_file_path):
    # Membaca semua data dari file input
    data = read_integers_from_file(input_file_path)
    M = int(data[0])  # Jumlah operasi
    commands = data[1:]  # Perintah-perintah berikutnya
    
    queue = deque()  # Antrian
    result = []  # Menyimpan hasil pengeluaran antrian
    
    for command in commands:
        if command.startswith('+'):
            # Menambahkan elemen ke antrian, pastikan ada angka setelah '+'
            parts = command.split()
            if len(parts) == 2:
                N = parts[1]
                queue.append(int(N))
        elif command == '-':
            # Mengeluarkan elemen dari antrian dan menyimpan hasilnya
            if queue:  # Pastikan antrian tidak kosong
                result.append(str(queue.popleft()))
    
    # Menyimpan hasil yang akan dicetak ke file output
    write_array_to_file(output_file_path, result)


def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task2'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    
    # Mengukur waktu eksekusi fungsi process_queue_operations
    measure_performance(process_queue_operations, input_file_path, output_file_path)


if __name__ == "__main__":
    main()


