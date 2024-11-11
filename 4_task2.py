# TODO импортировать необходимые молули


import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Открываем CSV файл для чтения
    with open(INPUT_FILENAME, "r") as input_file:
        # Открываем JSON файл для записи
        with open(OUTPUT_FILENAME, "w") as output_file:
            reader = csv.DictReader(input_file)
            data_list = []  # Список для хранения данных из CSV

            # Считываем строки из CSV файла
            for record in reader:
                data_list.append(record)

            # Сериализуем список данных в JSON файл с отступами для форматирования
            json.dump(data_list, output_file, indent=4)


if __name__ == '__main__':
    # Проверка работы функции
    task()

    # Чтение и вывод содержимого JSON файла
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
