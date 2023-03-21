age = int((input("Ваш возраст: ")))
growth = int((input("ваш рост: ")))
if age == 15 and growth < 160:
    print("чет ты маловат")
elif age == 15 and growth > 200:
    print("Фига ты высокий")
elif growth >= 220:
    print("Дяденька достань воробушка")
else:
    print("норм")