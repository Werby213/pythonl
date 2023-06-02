import tkinter as tk
import tkinter.filedialog as fd
import zipfile

# Пиздатая функция, которая сжимает эту хуйню
def compress_file():
    # Дерни путь к файлу, чтобы я знал, что за херь мы будем сжимать
    file_path = fd.askopenfilename()
    if file_path:
        # Определяем изначальный размер этой говнючки
        original_size = file_size(file_path)
        # Приколюха - добавим расширение .zip к имени файла, чтобы отличать сжатую хуйню
        compressed_file_path = file_path + ".zip"
        with zipfile.ZipFile(compressed_file_path, "w") as compressed_file:
            # Йобаный мастер, пишем эту пидорскую хуйню в сжатый файл
            compressed_file.write(file_path, compress_type=zipfile.ZIP_DEFLATED)
        # А теперь считаем размер сжатого пидараса
        compressed_size = file_size(compressed_file_path)
        # Здесь считаем процент сжатия. Знаешь, чтобы понять, на сколько меньше говна получилось после упаковки.
        compression_percent = (original_size - compressed_size) / original_size * 100
        # Покажем пользователю результаты, а то он нихуя не понимает
        result_text.set("Исходный размер: " + str(original_size) + " байт\n" +
                        "Сжатый размер: " + str(compressed_size) + " байт\n" +
                        "Процент сжатия: " + "{:.2f}".format(compression_percent) + "%")

# Чтобы тут распаковывать хуйню, ёпта
def extract_file():
    # Тут давай путь к сжатому файлу, а я его разархивирую
    file_path = fd.askopenfilename(filetypes=[("Zip files", "*.zip")])
    if file_path:
        with zipfile.ZipFile(file_path, "r") as compressed_file:
            # Весь этот ёбанный архив разворачиваем
            compressed_file.extractall()
        # Приколюха - выведем сообщение о том, что файл успешно извлечен
        result_text.set("Файл успешно извлечен, пиздуй дальше")

# Просто функция, которая возвращает размер этой залупы
def file_size(file_path):
    return sum(1 for _ in open(file_path, "rb"))

root = tk.Tk()
root.title("Сжатие и распаковка файлов")

# Ебаный кастомный баттон для сжатия
compress_button = tk.Button(root, text="Сжать", command=compress_file)
compress_button.pack()

# А вот и баттон для разархивации
extract_button = tk.Button(root, text="Разархивировать", command=extract_file)
extract_button.pack()

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

# Так, давай запускай это дерьмо и живи свободно, братан
root.mainloop()
