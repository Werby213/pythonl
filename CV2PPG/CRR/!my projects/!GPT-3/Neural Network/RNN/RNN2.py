import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import Input, LSTM, Dense
from tensorflow.keras.models import Model

import tensorflow_datasets as tfds

dataset = tfds.load("imdb_reviews", split="train[:80%]", as_supervised=True)
dataset = dataset.map(lambda x, y: x)


# Read dataset
text = dataset[0][0]
vocab = sorted(set(text))
text = [word for review in text for word in review]
char2idx = {u:i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

# Create sequences
text_as_int = np.array([char2idx[c] for c in text])
seq_length = 100
examples_per_epoch = len(text) // (seq_length + 1)

char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)
sequences = char_dataset.batch(seq_length + 1, drop_remainder=True)

def split_input_target(chunk):
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text, target_text

dataset = sequences.map(split_input_target).shuffle(10000).batch(64, drop_remainder=True)

# Create model
embedding_dim = 256
rnn_units = 1024

def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
  model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim,
                              batch_input_shape=[batch_size, None]),
    tf.keras.layers.LSTM(rnn_units,
                        return_sequences=True,
                        stateful=True,
                        recurrent_initializer='glorot_uniform'),
    tf.keras.layers.Dense(vocab_size)
  ])
  return model

model = build_model(len(vocab), embedding_dim, rnn_units, batch_size=64)

# Compile model
model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True))

# Train model
with tf.device('/GPU:0'):
    model.fit(dataset, epochs=10)

# Test model
model.evaluate(dataset)