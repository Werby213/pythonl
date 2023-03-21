import dearpygui.dearpygui as dpg
import numexpr
import keyboard
import time
def set_key(hotkey, ):
  key = keyboard.add_hotkey((input("Hotkey: ")))
def autokey(key, count, delay, start, stop):
  if start == 1:
    for i in range(count):
      keyboard.press(key)
      sleep(delay)
      keyboard.release(key)
      i+=1
  else:
    print("Autokey не запущен")
  elif:
    while stop == 0:
      keyboard.press(key)
      sleep(delay)
      keyboard.release(key)
dpg.create_viewport()
dpg.setup_dearpygui()
with dpg.window(label="Egor's autokey v1", height=200, width=500):
  key = dpg.add_input_float(label="Клавиша включения (или комбинация клавиш)", callback=autokey)
  count = dpg.add_input_int(label="Количество повторений (0=бесконечно)", callback=autokey)
  delay = dpg.add_input_int(label="Задержка в мс (0=без задержки)", callback=autokey)
  hotkey = dpg.add_input_str(label="Клавиша которая будет автоматически нажиматься", callback=set_key)
  start = dpg.add_button(label="Start", callback=autokey)
  stop = dpg.add_button(label="Stop", callback=autokey)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()