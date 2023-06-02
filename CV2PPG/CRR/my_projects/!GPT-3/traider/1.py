import pandas as pd

# получаем данные о ценах на акции
stock_data = pd.read_csv("stock_data.csv")

# находим максимальную и минимальную цену на акции
max_price = stock_data['Price'].max()
min_price = stock_data['Price'].min()

# находим разницу между максимальной и минимальной ценой
difference = max_price - min_price

# находим индекс наиболее выгодной цены
best_price_index = stock_data[stock_data['Price'] == min_price + difference/2].index[0]

# получаем наиболее выгодную цену
best_price = stock_data.loc[best_price_index]['Price']

# выводим наиболее выгодную цену для покупки
print("Наиболее выгодная цена для покупки: {}".format(best_price))