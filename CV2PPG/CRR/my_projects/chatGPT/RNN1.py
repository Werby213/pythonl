from keras.models import Sequential
from keras.layers import Dense, Activation

model = Sequential()
model.add(Dense(32, input_shape=(100,)))
model.add(Activation('relu'))
model.add(Dense(1))
model.add(Activation('sigmoid'))
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=5, batch_size=32)

# Оцениваем качество обучения на тестовых данных
loss, accuracy = model.evaluate(X_test, y_test)

# Проверка предсказания
test_set = np.array(["ты лох! потому что ты не можешь ничего доказать, и все твои ответы составляют только оскорбления!"])
prediction = model.predict(test_set)
print(prediction)