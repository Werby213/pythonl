import tensorflow as tf
from tensorflow import keras
# Define the model architecture
model = keras.models.Sequential([
    keras.layers.Dense(1, input_shape=(2,), activation='sigmoid')
])
# Compile the model
model.compile(optimizer=keras.optimizers.RMSprop(), loss='binary\_crossentropy', metrics=['accuracy'])
# Train the model on some data
x_train = np.array([[0, 0], [0, 1]]) # Example training data
y_train = np.array([[1], [0]]) # Corresponding labels
history = model.fit(x_train, y_train, epochs=5)
print('Training history: ', history.history)