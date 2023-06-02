import tkinter as tk
import openai
openai.api_key = "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"

# Импортируем необходимые библиотеки
import keyboard

# Создаём переменную для ввода задания
text = ''

# Создаём функцию для отображения поля ввода
def show_input_field():
    root = tk.Tk()
    root.title("OpenAI Task Input")

    # Создаем поле ввода
    entry = tk.Entry(root, width=50)
    entry.pack()

    # Создаем кнопку для подтверждения ввода
    btn = tk.Button(root, text="Done", command=lambda: get_text(entry))
    btn.pack()

    # Отображаем окно
    root.mainloop()

# Функция для получения введенного текста
def get_text(entry):
    global text
    text = entry.get()
    entry.delete(0, len(text))
    entry.destroy()

# Регистрируем сочетание клавиш для показа поля ввода
keyboard.add_hotkey('ctrl+shift+f12', show_input_field)

# Регистрируем сочетание клавиш для запуска нейросети
keyboard.add_hotkey('ctrl+shift+f11', lambda: keyboard.write(response.choices[0].text))

# Запускаем цикл слушания клавиатуры
keyboard.wait()