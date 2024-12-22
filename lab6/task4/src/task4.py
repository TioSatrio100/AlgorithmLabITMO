import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import read_file, write_output_file, measure_performance

def process_operations(input_file_path, output_file_path):
    n, operations = read_file(input_file_path)

    associative_map = {}
    insertion_order = []
    results = []

    for operation in operations:
        command = operation[0]
        key = operation[1]

        if command == "put":
            value = operation[2]
            if key not in associative_map:
                insertion_order.append(key)
            associative_map[key] = value

        elif command == "get":
            results.append(associative_map.get(key, "<none>"))

        elif command == "delete":
            if key in associative_map:
                del associative_map[key]
                insertion_order.remove(key)

        elif command == "prev":
            if key in associative_map:
                idx = insertion_order.index(key)
                if idx > 0:
                    prev_key = insertion_order[idx - 1]
                    results.append(associative_map[prev_key])
                else:
                    results.append("<none>")
            else:
                results.append("<none>")

        elif command == "next":
            if key in associative_map:
                idx = insertion_order.index(key)
                if idx < len(insertion_order) - 1:
                    next_key = insertion_order[idx + 1]
                    results.append(associative_map[next_key])
                else:
                    results.append("<none>")
            else:
                results.append("<none>")

    write_output_file(output_file_path, results)

def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task4'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    measure_performance(process_operations, input_file_path, output_file_path)

if __name__ == "__main__":
    main()

