import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(base_dir)

from utils import read_integers_space_from_file, write_array_to_file, measure_performance

def longest_increasing_subsequence(sequence):
    n = len(sequence)
    dp = [1] * n
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_length = max(dp)
    index = dp.index(max_length)

    subsequence = []
    while index != -1:
        subsequence.append(sequence[index])
        index = prev[index]

    subsequence.reverse()
    return max_length, subsequence

def process_file(input_file_path, output_file_path):
    n, sequence = read_integers_space_from_file(input_file_path)
    
    if sequence:
        length, subsequence = longest_increasing_subsequence(sequence)
        write_array_to_file(output_file_path, [length] + subsequence)
    else:
        write_array_to_file(output_file_path, [0])


def main():
    script_dir = os.path.dirname(__file__)
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'task6'))
    input_file_path = os.path.join(base_dir, 'txtf', 'input.txt')
    output_file_path = os.path.join(base_dir, 'txtf', 'output.txt')
    measure_performance(process_file, input_file_path, output_file_path)

if __name__ == "__main__":
    main()




