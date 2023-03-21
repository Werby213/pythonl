import cv2
import numpy as np

# Подключаем веб-камеру
cap = cv2.VideoCapture(0)

# Загружаем данные для обнаружения лиц
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Настраиваем границы фильтрации для дергания курсора
min_x = 0.0
min_y = 0.0
max_x = 1.0
max_y = 1.0

# Бесконечный цикл
while True:
    # Считываем кадр с веб-камеры
    _, frame = cap.read()
    # Преобразуем кадр в серые тона
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Обнаруживаем лицо на кадре
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        # Вычисляем центр лица
        x_center = x + w / 2
        y_center = y + h / 2
        # Вычисляем положение курсора относительно всего экрана
        x_pos = x_center / frame.shape[1]
        y_pos = y_center / frame.shape[0]
        # Фильтруем значения, чтобы курсор не дергался
        if x_pos > min_x and x_pos < max_x and y_pos > min_y and y_pos < max_y:
            min_x = x_pos - 0.1
            max_x = x_pos + 0.1
            min_y = y_pos - 0.1
            max_y = y_pos + 0.1
            # Перемещаем курсор на экране
            cv2.setMouseCallback("frame", lambda x, y: cv2.setMouseCallback("frame", x_pos, y_pos))
            # Отображаем лицо на кадре
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # Отображаем кадр
            cv2.imshow('frame', frame)

# Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()