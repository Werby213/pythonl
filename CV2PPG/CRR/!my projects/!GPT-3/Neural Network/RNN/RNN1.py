from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Загрузка датасета
dataset, info = tfds.load('text/gpt-3', with_info=True)

# Получить тренировочные и тестовые данные
train_dataset = dataset['train']
test_dataset = dataset['test']

# подготовка данных
tokenizer = tfds.features.text.SubwordTextEncoder.build_from_corpus(
    (article.numpy() for article in train_dataset), target_vocab_size=2**13)

# преобразование данных в последовательность индексов
def encode(article, summary):
  article = [tokenizer.vocab_size] + tokenizer.encode(article.numpy()) + [tokenizer.vocab_size+1]
  summary = [tokenizer.vocab_size] + tokenizer.encode(summary.numpy()) + [tokenizer.vocab_size+1]
  return article, summary

# паддинг
def filter_max_length(x, y, max_length=MAX_LENGTH):
  return tf.logical_and(tf.size(x) <= max_length,
                        tf.size(y) <= max_length)

# создание датасета
BATCH_SIZE = 64
BUFFER_SIZE = 20000
MAX_LENGTH = 40

train_dataset = train_dataset.map(lambda article, summary: encode(article, summary))
train_dataset = train_dataset.filter(filter_max_length)
# Склеивание последовательности
train_dataset = train_dataset.padded_batch(BATCH_SIZE, padded_shapes=([-1], [-1]))

# Инициализация модели
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(tokenizer.vocab_size+2, 64),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64,  return_sequences=True)),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(tokenizer.vocab_size+1, activation='softmax')
])

# Компиляция модели
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')

# Обучение модели
EPOCHS = 10
history = model.fit(train_dataset, epochs=EPOCHS)