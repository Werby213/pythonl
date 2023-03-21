import subprocess
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty

import os
import re
import webbrowser


class Notepad(App):
    font_size = 11
    debug = False
    start_message = "test"
    programming_language = ("Python", "C", "C++", "C#", "Pascal", "Basic")
    fonts = ("Arial", "Crixus", "Segoe", "Consolas")
    font = fonts[0]
    output = None
    error = None

    def file_size(self, file_path):
        return os.path.getsize(file_path)

    def select_font(self, font_name):
        self.font = font_name

    def replace(self, old, new):
        str_ = self.text1.text
        str_ = str_.replace(old, new)
        self.text1.text = str_

    def word_count(self):
        text = self.text1.text
        words = len(text.split())
        characters = len(text)
        lines = text.count("\n") + 1
        self.count.set(f"Слов: {words} Символов: {characters} Строк: {lines}")

    def increase_font_size(self):
        self.font_size += 1
        self.font_size_text = str(self.font_size)
        self.text1.update_from_scroll(1, 0, 0, 0)
        self.text1.tag_add("bigfont", "1.0", "end")
        self.text1.tag_configure("sel", font=(self.font, self.font_size))
        self.text1.tag_configure("bigfont", font=(self.font, self.font_size))
        self.select_font(self.sel_font.text)
        if self.debug is True:
            print(self.font_size, self.font)

    def decrease_font_size(self):
        self.font_size -= 1
        self.font_size_text = str(self.font_size)
        self.text1.tag_add("bigfont", "1.0", "end")
        self.text1.tag_configure("sel", font=(self.font, self.font_size))
        self.text1.tag_configure("bigfont", font=(self.font, self.font_size))
        self.text1.update_from_scroll(1, 0, 0, 0)
        self.select_font(self.sel_font.text)
        if self.debug is True:
            print(self.font_size, self.font)

    def run_code(self):
        text = self.text1.text
        process = subprocess.Popen(
            [self.select_programming_lang.text, "-c", text],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        self.output, self.error = process.communicate()
        if self.debug is True:
            print(self.output.decode("utf-8"))
            if self.error:
                print(colored("Subprocess", 'yellow'))
                print(colored(self.error.decode("utf-8"), 'red'))

    def refresh_console(self, text2):
        text2.readonly = False
        text2.text = ""
        output_text = self.output.decode("utf-8")
        if self.error:
            output_text = "Subprocess" + self.error.decode("utf-8")
        text2.text
