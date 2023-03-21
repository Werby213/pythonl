import random
i = 1
mode = int(input("число попыток(от 1 до 10): "))
comp = random.randint(1,mode)
score = 0
while i<10:
    hmn = int(input("угадай число: " ))
    if hmn > comp:
        print("меньше")
        score = score + 1
    elif hmn < comp:
        print("больше")
        score = score + 1
    else:
        print("ты победил")
        break
    if score == 10:
        print("ты проиграл")
        break
    i = i + 1
    print("использовано попыток:", score)