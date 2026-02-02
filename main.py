def calculate_and_report(input_file, output_file):
    # Открываем входной файл для чтения
    with open (input_file, "r") as file:
        numbers = [int(line.strip()) for line in file if line.strip().isdigit()]
    # Вычисляем сумму чисел в списке numbers
    total_sum = sum(numbers)
    # Вычисляем среднее значение; если список пустой, устанавливаем среднее равным 0
    average = total_sum / len(numbers) if numbers else 0

    # Открываем выходной файл для записи отчета
    with open (output_file, "w") as report:
        report.write(f"Total sum: {total_sum}, Average: {average}")

# Запускаем функцию с заданными именами входного и выходного файлов
calculate_and_report('data.txt', 'report.txt')