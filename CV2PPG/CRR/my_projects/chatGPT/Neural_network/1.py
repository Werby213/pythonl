import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow import keras
from tensorflow.keras.layers import Dense, Embedding, LSTM, Bidirectional
from tensorflow.keras.preprocessing.text import Tokenizer

# set GPU as device
tf.config.list_physical_devices('GPU')

# Prepare the data
chatbot_data = tfds.builder("imdb_reviews").as_dataset(split="train[:10%]", as_supervised=True)
tokenizer = Tokenizer()
tokenizer.fit_on_texts(chatbot_data)
data = tokenizer.texts_to_sequences(chatbot_data)

# Build the model
model = keras.Sequential()
model.add(Embedding(len(tokenizer.word_index)+1, 128))
model.add(Bidirectional(LSTM(64)))
model.add(Dense(64, activation='relu'))
model.add(Dense(len(tokenizer.word_index)+1, activation='softmax'))

# Compile and train the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(data, labels, epochs=10)
