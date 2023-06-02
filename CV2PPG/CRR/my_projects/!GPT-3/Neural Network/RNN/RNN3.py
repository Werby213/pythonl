# Импортируем библиотеки
import os
import numpy as np
import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, Dropout
from keras.utils.np_utils import to_categorical
from keras.callbacks import ModelCheckpoint

# Задаем параметры
batch_size = 32
epochs = 10

# Загружаем данные
data_dir = 'D:\\dataset1'
data_files = [os.path.join(data_dir,f) for f in os.listdir(data_dir)]

# Создаем массив с текстами
texts = []
for file in data_files:
    with open(file, 'r', encoding='utf-8') as f:
        texts.append(f.read())

# Векторизуем тексты
tokenizer = Tokenizer(num_words=None)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

# Делаем количество последовательностей равным
data = pad_sequences(sequences, maxlen=max([len(seq) for seq in sequences]))

# Создаем модель
model = Sequential()
model.add(Embedding(len(tokenizer.word_index)+1, 300, input_length=data.shape[1]))
model.add(LSTM(128, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(64))
model.add(Dropout(0.2))
model.add(Dense(len(tokenizer.word_index)+1, activation='softmax'))

# Компилируем модель
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Обучаем модель на GPU
model.fit(data, to_categorical(data), batch_size=batch_size, epochs=epochs, callbacks=[ModelCheckpoint('model.h5', monitor='val_acc', save_best_only=True)], validation_split=0.2, shuffle=True, use_multiprocessing=True, workers=4, verbose=1)