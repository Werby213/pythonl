import cv2

# Создаем объект класса VideoCapture для захвата видеопотока с камеры
cap = cv2.VideoCapture(0)

# Загружаем предварительно обученную модель Хаара для обнаружения лиц
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # Считываем кадр из видеопотока
    ret, frame = cap.read()

    # Конвертируем кадр в градации серого, чтобы упростить обработку
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Обнаруживаем лица на кадре с помощью каскада Хаара
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Применяем эффект пикселизации на обнаруженных лицах
    for (x, y, w, h) in faces:
        # Берем область изображения, содержащую только лицо
        face_roi = frame[y:y+h, x:x+w]
        # Применяем функцию пикселизации с коэффициентом масштабирования 10
        pixelated_face = cv2.resize(face_roi, (0,0), fx=0.1, fy=0.1, interpolation=cv2.INTER_NEAREST)
        # Заменяем оригинальное лицо на пикселизированное
        frame[y:y+h, x:x+w] = cv2.resize(pixelated_face, (w, h), interpolation=cv2.INTER_NEAREST)

    # Отображаем измененный кадр на экране
    cv2.imshow('Pixelated Faces', frame)

    # Ждем нажатия клавиши для выхода из программы
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем захват видео и закрываем окно
cap.release()
cv2.destroyAllWindows()
