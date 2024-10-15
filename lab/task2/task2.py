import os

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def main():
    base_dir = 'lab'
    input_file_path = os.path.join(base_dir, 'task2', 'input.txt')
    output_file_path = os.path.join(base_dir, 'task2', 'output.txt')

    try:
        with open(input_file_path, 'r') as file:
            n = int(file.read().strip())
            if n < 0 or n > 45:
                raise ValueError(f"Значение n ({n}) вне допустимого диапазона. Должно быть от 0 до 45.")
    except FileNotFoundError:
        print(f"Файл не найден: {input_file_path}")
        return
    except ValueError as e:
        print(f"Ошибка при чтении или проверке данных: {e}")
        return

    result = fibonacci_iterative(n)

    try:
        with open(output_file_path, 'w') as file:
            file.write(f"{result}\n")
    except IOError:
        print(f"Произошла ошибка при записи в файл: {output_file_path}")

if __name__ == "__main__":
    main()
