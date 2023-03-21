import tkinter as tk
import tkinter.filedialog as fd
import zipfile

def compress_file():
    file_path = fd.askopenfilename()
    if file_path:
        original_size = file_size(file_path)
        compressed_file_path = file_path + ".zip"
        with zipfile.ZipFile(compressed_file_path, "w") as compressed_file:
            compressed_file.write(file_path, compress_type=zipfile.ZIP_DEFLATED)
        compressed_size = file_size(compressed_file_path)
        compression_percent = (original_size - compressed_size) / original_size * 100
        result_text.set("Original size: " + str(original_size) + " bytes\n" +
                        "Compressed size: " + str(compressed_size) + " bytes\n" +
                        "Compression percent: " + "{:.2f}".format(compression_percent) + "%")

def extract_file():
    file_path = fd.askopenfilename(filetypes=[("Zip files", "*.zip")])
    if file_path:
        with zipfile.ZipFile(file_path, "r") as compressed_file:
            compressed_file.extractall()
        result_text.set("File extracted successfully")

def file_size(file_path):
    return sum(1 for _ in open(file_path, "rb"))

root = tk.Tk()
root.title("File Compression and Extraction")

compress_button = tk.Button(root, text="Compress", command=compress_file)
compress_button.pack()

extract_button = tk.Button(root, text="Extract", command=extract_file)
extract_button.pack()

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

root.mainloop()
