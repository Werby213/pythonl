from beamngpy import BeamNGpy, Vehicle, Scenario
import time
import math
# Создание экземпляра BeamNGpy
beamng = BeamNGpy('localhost', 64256, home='E:/Games/SteamApps/common/BeamNG.drive', user='E:/Games/BeamNG.drive_DATA/0.28')

# Создание сценария
scenario = Scenario('west_coast_usa', 'example')

# Создание машины
vehicle = Vehicle('ego_vehicle', model='etk800', licence='PYTHON')
scenario.add_vehicle(vehicle, pos=(-717, 101, 118), rot_quat=(0, 0, 0.3826834, 0.9238795))

# Запуск симулятора и сценария
beamng.open()
scenario.make(beamng)
beamng.scenario.load(scenario)
beamng.scenario.start()

# Определение целевой позиции для машины
target_pos = (200, 0, 0)

# Определение ИИ-алгоритма
while True:
    vehicle.update_vehicle()
    sensors_data = vehicle.get_sensor_data()
    obstacles = sensors_data['front_cam']['depth']
    speed_limit = 50
    desired_speed = speed_limit
    desired_angle = 0
    if obstacles[80][40] < 30:
        desired_speed = 0
    elif obstacles[80][40] < 50:
        desired_speed *= obstacles[80][40] / 50
        desired_angle = -(40 - obstacles[80].index(min(obstacles[80]))) / 40
    vehicle.control(throttle=0.5, steering=desired_angle, brake=0, handbrake=False)
    time.sleep(0.1)

    time.sleep(0.1)

# Остановить симулятор и закрыть соединение
beamng.stop_scenario()
beamng.close()
