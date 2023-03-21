import winsound
import time

# Функция для воспроизведения звука с определенной частотой и продолжительностью
def play_sound(frequency, duration):
    winsound.Beep(frequency, duration)

# Пример создания мелодии, используя функцию play_sound
play_sound(262, 250) # Do
play_sound(294, 250) # Re
play_sound(330, 250) # Mi
time.sleep(0.1)
play_sound(349, 250) # Fa
time.sleep(0.1)
play_sound(392, 250) # Sol
play_sound(440, 250) # La
play_sound(494, 250) # Si
time.sleep(0.1)
play_sound(523, 250) # Do
