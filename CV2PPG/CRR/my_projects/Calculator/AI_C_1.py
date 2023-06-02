import tkinter as tk
class Calculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.pack()

        # Create buttons for basic arithmetic operations (+,-,\*,/)
        self.add_button = tk.Button(self, text="+", command=lambda: self._execute("1"))
        self.subtract_button = tk.Button(self, text="-', command=lambda: self._execute("2"))
        self.multiply_button = tk.Button(self, text="*", command=lambda: self._execute("3"))
        self.divide_button = tk.Button(self, text="/", command=lambda: self._execute("4"))

        # Add labels for result display
        self.result_label = tk.Label(self, text="0")
        self.result_entry = tk.Entry(self, width=8)

        # Pack elements onto frame
        self.add_button.pack(side='left')
        self.subtract_button.pack(side='right')
        self.multiply_button.pack(side='bottom')
        self.divide_button.pack(side='top')
        self.result_label.pack(side='left', fill='x')
        self.result_entry.pack(fill='both', expand=True)

    def _execute(self, operation):
        """Execute given math operation"""
        if not self.text:  # check if entry has any value
            return "Please enter a number."

        num1 = float(self.text)  # convert text to float
        operator = {'+': 'add', '-':'subtract', '\*':'multiply', '/': 'divide'}[operation]  # set operator based on button pressed

        try:
            num2 = eval(f"{operator}(num1)")  # execute math operation

            # update label with result
            self.result_label['text'] = f"{num1} {operator} {num2}"
        except ZeroDivisionError:
            print("Cannot divide by zero.")
            return "Invalid input."


