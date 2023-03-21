def return_name_and_age(name, age):
    print("Меня зовут",name,", мне", age,"лет")
    if age >= 18:
        print("Я хочу спать")
    else:
        print("До 18 лет осталось: ", 18 - age)
name_user = input("Имя: ")
age_user = int(input("Возраст: "))
return_name_and_age(name_user, age_user)