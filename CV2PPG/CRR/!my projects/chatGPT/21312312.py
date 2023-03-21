import tensorflow as tf

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(10, input_shape=(3,)))
model.add(tf.keras.layers.Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')

# Имитация данных для обучения
x_train = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]
y_train = [[0.2], [0.4], [0.6]]

# Обучение модели
model.fit(x_train, y_train, epochs=100)
