import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import read_lines_from_file, write_array_to_file, measure_performance

def count_segments_covering_points(segments, points):
    events = []
    result = [0] * len(points)

    for start, end in segments:
        events.append((start, 'L'))
        events.append((end + 1, 'R'))

    for idx, point in enumerate(points):
        events.append((point, 'P', idx))

    events.sort()

    active_segments = 0
    for event in events:
        if event[1] == 'L':
            active_segments += 1
        elif event[1] == 'R':
            active_segments -= 1
        elif event[1] == 'P':
            _, _, idx = event
            result[idx] = active_segments

    return result


def process_file(input_file_path, output_file_path):
    lines = read_lines_from_file(input_file_path)
    s, p = map(int, lines[0].split())

    segments = []
    for i in range(1, s + 1):
        a, b = map(int, lines[i].split())
        segments.append((a, b))

    points = list(map(int, lines[s + 1].split()))

    result = count_segments_covering_points(segments, points)
    write_array_to_file(output_file_path, result)


def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task4'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    measure_performance(process_file, input_file_path, output_file_path)


if __name__ == "__main__":
    main()
