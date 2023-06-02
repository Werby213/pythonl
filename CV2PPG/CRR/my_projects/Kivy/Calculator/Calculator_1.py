import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class CalculatorApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')
        display = TextInput(font_size=30, size_hint_y=None, height=100, text='0')
        layout.add_widget(display)
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+']
        ]
        for row in buttons:
            r = BoxLayout()
            for label in row:
                button = Button(text=label, font_size=30)
                button.bind(on_press=self.button_pressed)
                r.add_widget(button)
            layout.add_widget(r)
        equals_button = Button(text='=', font_size=30)
        equals_button.bind(on_press=self.calculate)
        layout.add_widget(equals_button)
        return layout

    def button_pressed(self, button):
        current = self.root.ids.display.text
        if current == '0':
            self.root.ids.display.text = ''
            self.root.ids.display.text += button.text
        else:
            self.root.ids.display.text += button.text

    def calculate(self, instance):
        try:
            self.root.ids.display.text = str(eval(self.root.ids.display.text))
        except:
            self.root.ids.display.text = 'Error'

if __name__ == '__main__':
    CalculatorApp().run()
