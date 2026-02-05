import csv
import os

# Определяем имя файла, с которым будем работать
filename = 'students.csv'

file_exists = os.path.exists(filename)
file_empty = not file_exists or os.stat(filename).st_size == 0
# Создаем пустой список для хранения информации о студентах
students = []

# Чтение данных студентов из CSV-файла
with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
    # Создаем объект csvreader для чтения строк из файла
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        # Проверяем, что в строке ровно 3 элемента (имя, возраст, курс)
        if len(row) == 3:
            # Добавляем данные студента в список в виде словаря
            students.append({
                'name': row[0],
                'age': row[1],
                'course': row[2]
            })

# Пример добавления нового студента
students.append({'name': 'John Doe', 'age': '22', 'course': 'Physics'})

# Запись обновленных данных студентов в CSV-файл
with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
    # Создаем объект csvwriter для записи строк в файл
    csvwriter = csv.DictWriter(csvfile, fieldnames=["name", "age", "course"])
    # Записываем данные каждого студента в файл
    if file_empty:
        csvwriter.writeheader()
    csvwriter.writerows(students)