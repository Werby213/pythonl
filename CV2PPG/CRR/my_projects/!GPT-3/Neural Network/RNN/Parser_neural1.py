import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Функция для парсинга сайтов
def parse_site(url):
    response = requests.get("https://ru.wikipedia.org")
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.find_all(text=True)
    visible_text = filter(visible, text)
    return " ".join(t.strip() for t in visible_text)

# Функция для предварительной обработки текста
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9]', ' ', text) # удаляем все символы кроме букв и цифр
    text = re.sub(r'\s+', ' ', text) # удаляем лишние пробелы
    text = text.strip()
    return text

# Функция для выделения видимого текста
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True

# Функция для создания модели
def create_model():
    model = Sequential()
    model.add(Embedding(vocab_size, 50, input_length=max_len-1))
    model.add(LSTM(128))
    model.add(Dense(vocab_size, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# Функция для обучения модели
def train_model():
    # Создаем модель
    model = create_model()
    # Обучаем модель
    model.fit(X, y, epochs=50, verbose=2)
    # Сохраняем модель
    model.save('model.h5')

# Основная функция
def main():
    # Получаем список ссылок
    links = get_links()
    # Получаем словарь слов
    words = get_words(links)
    # Создаем индекс для слов
    word_index = create_word_index(words)
    # Преобразуем текст в последовательность слов
    sequences = create_sequences(word_index)
    # Определяем размерность словаря и максимальную длину
    vocab_size = len(word_index) + 1
    max_len = max([len(seq) for seq in sequences])
    # Преобразуем последовательности в матрицу
    X, y = create_matrix(sequences, vocab_size, max_len)
    # Обучаем модель
    train_model(X, y, vocab_size, max_len)

if __name__ == '__main__':
    main()