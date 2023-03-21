import tensorflow as tf
import numpy as np

# Set up the game board
board = np.zeros((10, 10), dtype=np.int32)
board[3, 5:8] = 1
board[4:6, 6] = 1

# Set up the TensorFlow graph
input_board = tf.Variable(initial_value=tf.zeros(shape=[None, None], dtype=tf.int32))kernel = tf.constant(np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=np.int32), dtype=tf.int32)
neighbor_counts = tf.nn.conv2d(tf.expand_dims(tf.expand_dims(tf.cast(input_board, tf.float32), 0), -1),
                                tf.expand_dims(tf.expand_dims(tf.cast(kernel, tf.float32), -1), -1),
                                strides=[1, 1, 1, 1], padding='SAME')
alive_mask = tf.logical_or(tf.equal(input_board, 1), tf.equal(neighbor_counts, 3))
next_board = tf.cast(tf.logical_and(alive_mask, tf.not_equal(neighbor_counts, 2)), tf.int32)

# Run the TensorFlow graph to get the next board state
with tf.Session() as sess:
    for i in range(10):
        print('Generation', i)
        print(board)
        board = sess.run(next_board, feed_dict={input_board: board})
def display_board(board):
    tf.compat.v1.disable_eager_execution()
    session = tf.compat.v1.Session()
    board = np.array(board, dtype=np.int32)
    board_placeholder = tf.compat.v1.placeholder(tf.int32, board.shape)
    board_image = tf.expand_dims(tf.cast(board_placeholder, tf.float32), axis=-1)
    summary_op = tf.compat.v1.summary.image("board", board_image)
    summary = session.run(summary_op, feed_dict={board_placeholder: board})
    writer = tf.compat.v1.summary.FileWriter('logdir')
    writer.add_summary(summary)
    writer.close()