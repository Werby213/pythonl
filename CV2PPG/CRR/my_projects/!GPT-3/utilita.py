import keyboard
import openai

openai.api_key = "<OpenAI API Key>"

def on_hotkey_task():
    task = input("Enter task for AI: ")
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=task,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
    ).choices[0].text
    keyboard.write(response)

keyboard.add_hotkey('ctrl+shift+f12', on_hotkey_task)

keyboard.wait()
