import os
import random

#this program is made to create maximum input of each existing task so that it is not done manually. 
def generate_max_input():
    base_dir = 'lab1/task1'
    os.makedirs(base_dir, exist_ok=True)
    
    n = 1000
    arr = ' '.join(map(str, random.sample(range(n), n)))  

    input_file_path = os.path.join(base_dir, 'input.txt')
    
    with open(input_file_path, 'w') as file:
        file.write(f"{n}\n{arr}\n")  

if __name__ == "__main__":
    generate_max_input()
