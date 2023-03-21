import openai

# Initialize API key
openai.api_key = "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"
import tkinter as tk


def main():
    global text

    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    text = tk.StringVar()
    entry = tk.Entry(frame, textvariable=text)
    entry.pack()

    # Отслеживаем нажатие сочетания клавиш
    root.bind('<Control-Shift-F12>', lambda event: openai_completion())
    root.mainloop()


# Функция openai_completion принимает введенное пользователем задание и отправляет его на OpenAI API
def openai_completion():
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text.get(),
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    # Печатает ответ на задание
    print(response["choices"][0]["text"])
    root.destroy()


if __name__ == "__main__":
    main()

