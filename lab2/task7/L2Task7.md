# Задание №7 по варианту : `Поиск максимального подмассива за линейное время`

Студент ИТМО, Субагио Сатрио 467615

## Вариант 16

## Задание 7 Поиск максимального подмассива за линейное время

Можно найти максимальный подмассив за линейное время, воспользовавшись
следующими идеями. Начните с левого конца массива и двигайтесь вправо, отслеживая найденный к данному моменту максимальный подмассив. Зная максимальный подмассив массива A[1..j], распространите ответ на поиск максимального
подмассива, заканчивающегося индексом j + 1, воспользовавшись следующим
наблюдением: максимальный подмассив массива A[1..j + 1] представляет собой
либо максимальный подмассив массива A[1..j], либо подмассив A[i..j + 1] для
некоторого 1 ≤ i ≤ j + 1. Определите максимальный подмассив вида A[i..j + 1]
за константное время, зная максимальный подмассив, заканчивающийся индексом
j.
В этом случае у вас возможны 2 варианта тестирования: первый предполагает
создание рандомного массива чисел, аналогично задаче №1 (в этом случае формат входного и выходного файла смотрите там). Второй вариант - взять любые
данные по акциям какой-либо компании, аналогично задаче №6.

## Input / Output

| Input               | Output                             |
| ------------------- | ---------------------------------- |
| `date,price`        | `Компания: Tesla`                  |
| `2024-10-01,258.02` | `Период: 2024-10-01 до 2024-10-15` |
| `2024-10-02,249.02` | `Дата покупки: 2024-10-01`         |
| `2024-10-03,240.66` | `Дата продажи: 2024-10-15`         |
| `2024-10-04,250.08` | `Максимальная прибыль: 2615.79`    |
| `2024-10-07,240.83` |                                    |
| `2024-10-08,240.83` |                                    |
| `2024-10-09,241.05` |                                    |
| `2024-10-10,238.77` |                                    |
| `2024-10-11,217.80` |                                    |
| `2024-10-14,219.16` |                                    |
| `2024-10-15,219.57` |                                    |

## Ограничения по времени и памяти

- Ограничение по времени. 0.001312 секунд.
- Ограничение по памяти. 1080 байт.

## Запуск проекта

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/TioSatrio100/AlgorithmLabITMO.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd lab2/task7
   ```
3. Запустите программу:

   ```bash
   python src/task7.py
   ```

4. Запуск тестов:
   ```bash
   python tests/task7.py
   ```

## Тестирование

Для запуска тестов выполните:

```bash
   python -m unittest tests test7.py
```
