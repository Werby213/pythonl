import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Считываем данные из Excel-файла
df = pd.read_excel('data.xlsx')

# Визуализация данных
plt.scatter(df['Date'], df['Price'])
plt.show()

# Создаем массив признаков и целевой массив
X = df['Date'].values.reshape(-1, 1)
y = df['Price'].values

# Обучаем модель линейной регрессии на данных
model = LinearRegression()
model.fit(X, y)

# Предсказываем цены на следующие даты
future_dates = np.array([2022, 2023, 2024]).reshape(-1, 1)
future_prices = model.predict(future_dates)

# Выводим предсказанные цены
for i, price in enumerate(future_prices):
    print(f"Predicted price for year {2022 + i}: {price}")
