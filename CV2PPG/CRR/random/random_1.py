import random
i = 1
l1 = ["Ученый", "Больной", "Пикачу", "Кот", "Никто", "Террорист", "Сантехник", "Динозавр", "Мама", "Менеджер"]
l2 = ["приходит в офис","приходит в небытие","приходит в больницу","приходит дратся","приходит в лабораторию","приходит на вызов","приходит в парк юрского периода","приходит на родительское собрание","приходит к кошке","приходит в метро"]
l3 = ["и говорит я совершил открытие","и говорит ПИКА-ПИКА!","и говорит мысленно привет, НИЧТО","и говорит у меня болит голова","и говорит давай заведем котят","и говорит я мама вовочки","и говорит я увольняюсь!","и говорит ВСЕ НА СУББОТНИК!","и говорит возьмите меня есть туристов","и говорит какой серьезный засор"]
l4 = ["а кошка отвечает","а учительница:","а небытие ему в ответ","а доктора ему","а тут по громкоговорителю","а ученое сообщество:","а в ответ слышит","а из трубы голос","а начальник ему","а бульбазавр на это"]
l5 = ["... ты не пикачу, ты сантехник","... я не доктор, я динозавр","... давай лучше мышат","... привет ничтожество","... следующая станция бесконечная","... вы не мама вы папа","... нам такие не нужны","... ты же на пенсию вышел","... ты новый Энштейн","... ну хочешь шутку расскажу"]
l6 = ["энтропия нарастала","и уехали в Казахстан","диназавр всеравно сьел туристов","держите пятюню","и все стали танцевать","вот и сказочке конец","так появилась вселенная","с тех пор это закон","и немедленно запрыгал","LOL )))"]
while i<7:
    print(random.choice(globals().get("l"+str(i))))
    i = i + 1