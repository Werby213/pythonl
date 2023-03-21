print("Введите пароль:")
guess=input()
password='test'
attempts = 5
i = 1
while guess!=password and i<attempts:
    print("Неправильный пароль")
    guess=input()
    i = i + 1
if guess == password:
    print("Правильный пароль")
else:
    print("Вы 5 раз ввели неправильный пароль")