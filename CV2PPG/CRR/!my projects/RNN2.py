import tensorflow as tf

# размер батча
batch_size = 32
# размер входных данных
sequence_length = 50
input_dim = 100
# размер скрытого слоя
hidden_dim = 60
# размер выходных данных
output_dim = 10

# открываем граф для нахождения весов
X = tf.placeholder(tf.float32, [None, sequence_length, input_dim])
Y = tf.placeholder(tf.float32, [None, output_dim])

# Установка схемы весов
# define the weights
weights = {"out": tf.Variable(tf.random_normal([hidden_dim, output_dim], mean=0, stddev=.01))}
biases = {"out": tf.Variable(tf.random_normal([output_dim], mean=0, stddev=.01))}


# создание скрытого слоя
def recurrentNetwork(x):
    # создание переменной для слоя
    layer = {'weights': tf.Variable(tf.random_normal([input_dim + hidden_dim, hidden_dim], mean=0, stddev=.01)),
             'biases': tf.Variable(tf.random_normal([hidden_dim], mean=0, stddev=[input_dim + hidden_dim]))}

    # организуем структуру для переменной
    state = tf.zeros([batch_size, hidden_dim])
    for t in range(sequence_length):
        # конкатенирование образцов
        x_t = tf.concat([x[:, t, :], state], -1)

        # умножаем переменную для слоя на веса и вычисляем значение для него
        state = tf.tanh(tf.matmul(x_t, layer['weights']) + layer['biases'])

    # умножаем скрытый слой на выходные данные и добавляем веса
    output = tf.matmul(state, weights['out'] + biases['out'])
    return output


# предсказание выходных данных
logits = recurrentNetwork(X)

# настройка потерь
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y))

# вычисление точности
accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(logits, 1), tf.argmax(Y, 1)), tf.float32))

# выбор оптимизатора
optimizer = tf.train.AdamOptimizer().minimize(loss)

# инициализация переменных
init = tf.global_variables_initializer()

# запуск графа
with tf.Session() as sess:
    sess.run(init)
    # обучение и тестирование нейронной сети
    for epoch in range(num_epochs):
        for i in range(total_batch):
            # настраиваем batch для обучения
            batch_x, batch_y = mnist.train.next_batch(batch_size)
            # выполняем обучение
            sess.run(optimizer, feed_dict={X: batch_x, Y: batch_y})
            # вычисляем точность
            train_loss, train_accuracy = sess.run([loss, accuracy],
                                                  feed_dict={X: batch_x, Y: batch_y})
        # выводим прогресс обучения
        print("epoch :{}, loss : {:.4f}, accuracy : {:.2f}%".format(epoch + 1,
                                                                    train_loss, train_accuracy * 100))
    # тестирования нейронной сети
    test_accuracy = sess.run(accuracy, feed_dict={X: mnist.test.images, Y: mnist.test.labels})
    print("accuracy : {:.2f}%".format(test_accuracy * 100))