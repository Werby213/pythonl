import pyautogui
import statistics

# Установить время, в течение которого будут собираться данные
time_interval = 5

# Собрать данные о движении мыши в течение определенного времени
mouse_data = pyautogui.getMovement(time_interval=time_interval)

# Создать список, содержащий значения скорости мыши
speed_list = []
for data in mouse_data:
    speed = data[2]
    speed_list.append(speed)

# Найти наивысшее значение скорости
highest_speed = max(speed_list)

# Вывести результат
print("Наивысшее значение скорости мыши за {} секунд составляет {} пикселей в секунду".format(time_interval, highest_speed))
