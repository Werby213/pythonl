import tensorflow as tf
import os
import numpy as np
import gpt_2_simple as gpt2

# Путь к папке с моделью
model_name = "355M"
model_path = os.path.join("models", model_name)

# Загрузка модели
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, model_name=model_name, model_dir=model_path)

# Генерация текста
generated_text = gpt2.generate(sess, model_name=model_name, model_dir=model_path, prefix="Hello, world!", length=1023, temperature=0.7, nsamples=1, batch_size=1, return_as_list=True)[0]

print(generated_text)
