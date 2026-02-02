import pandas as pd

# Загрузка данных из Excel-файла
file_path = 'financial_report.xlsx'
sheet_name = 'Операции'
column_name = 'Доход'

# Чтение данных из указанного листа

data = pd.read_excel(file_path, sheet_name=sheet_name)
# Выбор колонки "Доход"
income_data = data[column_name]

# Вычисление минимального, максимального и среднего дохода
max_income = income_data.max()
min_income = income_data.min()
mean_income = income_data.mean()
# Вывод результатов на экран
print(f"Минимальный доход: {min_income}")
print(f"Максимальный доход: {max_income}")
print(f"Средний доход: {mean_income}")