# Задание №1 по варианту : `Сортировка слиянием`

Студент ИТМО, Субагио Сатрио 467615

## Вариант 16

## Задание 1 Сортировка слиянием

. Используя псевдокод процедур Merge и Merge-sort из презентации к Лекции 2 (страницы 6-7), напишите программу сортировки слиянием на Python и
проверьте сортировку, создав несколько рандомных массивов, подходящих
под параметры:
• Формат входного файла (input.txt). В первой строке входного файла
содержится число n (1 ≤ n ≤ 2 · 104
) — число элементов в массиве.
Во второй строке находятся n различных целых чисел, по модулю не
превосходящих 109
.
• Формат выходного файла (output.txt). Одна строка выходного файла
с отсортированным массивом. Между любыми двумя числами должен
стоять ровно один пробел.
• Ограничение по времени. 2сек.
• Ограничение по памяти. 256 мб.

## Input / Output

| Input     | Output    |
| --------- | --------- |
| 5         | 1 2 3 4 5 |
| 4 1 2 3 5 |           |
|           |           |

## Ограничения по времени и памяти

- Ограничение по времени. 0.001199 секунд.
- Ограничение по памяти. 896 байт.

## Запуск проекта

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/TioSatrio100/AlgorithmLabITMO.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd lab2/task1
   ```
3. Запустите программу:

   ```bash
   python src/task1.py
   ```

4. Запуск тестов:
   ```bash
   python tests/task1.py
   ```

## Тестирование

Для запуска тестов выполните:

```bash
   python -m unittest tests test1.py
```