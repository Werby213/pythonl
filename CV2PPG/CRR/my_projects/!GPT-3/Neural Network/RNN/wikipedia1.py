import wikipedia
import tensorflow as tf
import numpy as np

# получаем данные из wikipedia
pages = wikipedia.page("DeepMind")

# Создаем переменную для хранения данных из википедии
data = pages.content

# Разбиваем данные на массивы
data = data.split("\n")

# Создаем переменную для векторизации данных
data = np.array(data)

# Векторизируем данные
data = np.vectorize(data)

# Создаем модель сети
model = tf.keras.Sequential()

# Добавляем уровни слоев в модель
model.add(tf.keras.layers.Dense(units=1024, activation='relu', input_dim=data.shape[1]))
model.add(tf.keras.layers.Dense(units=512, activation='relu'))
model.add(tf.keras.layers.Dense(units=256, activation='relu'))
model.add(tf.keras.layers.Dense(units=128, activation='relu'))
model.add(tf.keras.layers.Dense(units=1, activation='linear'))

# Компилируем модель
model.compile(loss='mse',
              optimizer='adam',
              metrics=['accuracy'])

# Ищем все GPU доступные на компьютере и делаем их доступными для обучения
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
  try:
    # Назначаем доступные GPU для обучения
    for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)
    logical_gpus = tf.config.experimental.list_logical_devices('GPU')
    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
  except RuntimeError as e:
    # Выводим сообщение об ошибке если происходит ошибка
    print(e)

# Тренируем модель
model.fit(data, epochs=50, batch_size=32)

# Сохраняем модель
model.save('deepmind_model.h5')

print('Model saved!')