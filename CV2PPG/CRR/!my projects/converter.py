
from tkinter import *
import requests

root = Tk()
root.title("Currency converter")
root.geometry("400x200")

def convert():
    from_cur = from_currency.get()
    to_cur = to_currency.get()
    amount = amount_entry.get()
    response = requests.get(f'http://api.exchangeratesapi.io/latest?base={from_cur}')
    data = response.json()
    rate = data['rates'][to_cur]
    result = float(amount) * rate
    answer_label.config(text=f"Result: {amount} {from_cur} = {result} {to_cur}")

Label(root, text="Currency converter").grid(row=0, column=0, columnspan=2)

amount_label = Label(root, text="Enter amount")
amount_label.grid(row=1, column=0)

amount_entry = Entry(root)
amount_entry.grid(row=1, column=1)

from_currency = StringVar(root)
from_currency.set("USD")

from_label = Label(root, text="From")
from_label.grid(row=2, column=0)

from_menu = OptionMenu(root, from_currency, "USD", "EUR", "GBP", "HKD", "JPY", "CAD", "INR")
from_menu.grid(row=2, column=1)

to_label = Label(root, text="To")
to_label.grid(row=3, column=0)

to_currency = StringVar(root)
to_currency.set("EUR")

to_menu = OptionMenu(root, to_currency, "USD", "EUR", "GBP", "HKD", "JPY", "CAD", "INR")
to_menu.grid(row=3, column=1)

convert_button = Button(root, text="Convert", command=convert)
convert_button.grid(row=4, column=0, columnspan=2)

answer_label = Label(root, text="")
answer_label.grid(row=5, column=0, columnspan=2)

root.mainloop()