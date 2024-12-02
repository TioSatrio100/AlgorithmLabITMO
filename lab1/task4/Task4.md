# Задание №4 по варианту : ` Линейный поиск`

Студент ИТМО, Субагио Сатрио 467615

## Вариант 16

## Задание 4 Линейный поиск

Рассмотрим задачу поиска.
• Формат входного файла. Последовательность изn чисел A = a1, a2, . . . , an
в первой строке, числа разделены пробелом, и значение V во второй строке.
Ограничения: 0 ≤ n ≤ 103
, −103 ≤ ai
, V ≤ 103
• Формат выходного файла. Одно число - индекс i, такой, что V = A[i],
или значение −1, если V в отсутствует.
• Напишите код линейного поиска, при работе которого выполняется сканирование последовательности в поисках значения V .
• Если число встречается несколько раз, то выведите, сколько раз встречается
число и все индексы i через запятую.
• Дополнительно: попробуйте найти свинью, как в лекции. Используйте во
входном файле последовательность слов из лекции, и найдите соответствующий индекс.

## Input / Output

| Input                   | Output |
| ----------------------- | ------ |
| 2 5 632 65 342 23 23 40 | 6 7    |
| 23                      |        |
|                         |        |

## Ограничения по времени и памяти

- Ограничение по времени. 0.000859 секунд.
- Ограничение по памяти. 2196 байт.

## Запуск проекта

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/TioSatrio100/AlgorithmLabITMO.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd lab1/task4
   ```
3. Запустите программу:

   ```bash
   python src/task4.py
   ```

4. Запуск тестов:
   ```bash
   python tests/test_task4.py
   ```

## Тестирование

Для запуска тестов выполните:

```bash
   python -m unittest tests test_task4.py
```