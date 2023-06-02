import time
from beamngpy import BeamNGpy, Vehicle, Scenario
import numpy as np

# Создание экземпляра BeamNGpy
beamng = BeamNGpy('localhost', 64256, home='E:/Games/SteamApps/common/BeamNG.drive', user='E:/Games/BeamNG.drive_DATA/0.28')

# Создание сценария
scenario = Scenario('west_coast_usa', 'obstacle_course')
road_a = scenario.add_road('A', looped=False)
road_a.add_lane([-60, 0, 0], [60, 0, 0], width=4)

# Создание машины
vehicle = Vehicle('ego_vehicle', model='etk800', licence='PYTHON')
scenario.add_vehicle(vehicle, pos=(-717, 101, 118), rot_quat=(0, 0, 0.3826834, 0.9238795))

# Запуск симулятора и сценария
beamng.open()
beamng.load_scenario(scenario)
beamng.start_scenario()


# Функция, которая будет вызываться каждый кадр симуляции
def update():
    # Получение текущего положения и угла поворота машины
    pos = vehicle.state['pos']
    dir_vec = vehicle.state['dir']
    yaw = vehicle.state['yaw']

    # Определение направления, в котором машина будет двигаться вперед
    fwd_vec = [np.cos(yaw), np.sin(yaw), 0]

    # Определение точки, куда машина будет двигаться
    target_pos = pos + np.array(fwd_vec) * 50

    # Получение списка препятствий
    obstacles = beamng.get_objects(vehicle, dist=50, exclude=['static'])

    # Если есть препятствия, выбираем ближайшее и вычисляем курс машины, чтобы объезжать его
    if obstacles:
        nearest_obstacle = obstacles[0]
        obstacle_pos = nearest_obstacle['pos']
        obstacle_dist = np.linalg.norm(obstacle_pos - pos)
        obstacle_vec = obstacle_pos - pos
        left_vec = np.array([-dir_vec[1], dir_vec[0], 0])
        left_vec = left_vec / np.linalg.norm(left_vec)
        target_pos = pos + dir_vec * obstacle_dist + left_vec * 10

    # Направление, в котором машина будет двигаться
    target_dir = target_pos - pos
    target_dir /= np.linalg.norm(target_dir)

    # Установка угла поворота для машины
    dot = np.dot(target_dir, fwd_vec)
    cross = np.cross(target_dir, fwd_vec)
    angle = np.arccos(dot)
    if cross[2] < 0:
        angle = -angle
    vehicle.control('steering', angle)

    # Установка скорости для машины
    vehicle.control('throttle', 1)
    vehicle.control('brake', 0)
    vehicle.control('clutch', 0)


# Запуск симуляции
vehicle.ai_set_mode('manual')
vehicle.control('manual_gearbox_clutch', 1