story = "Вы проснулись в темной комнате. Вы не знаете, где вы находитесь. Вы видите дверь справа, окно слева, шкаф напротив и кровать под вами."
options = "1. Попытаться открыть дверь\n2. Попытаться выбить окно\n3. Исследовать шкаф\n4. Лечь и поспать"
class mainstory:
    def story_options():
        global story, options, choice
        print(story)
        print(options)
        choice = input("Что вы выбираете? ")
        if choice == "1":
            self.c1 = c1
            print(self.c1)
while True:
    print(story)
    print(options)
    choice = input("Что вы выбираете? ")

    if choice == "1":
        story += "\nВы пытаетесь открыть дверь, но она заперта."
        options = "1. Посмотреть через замочную скажину что за дверью\n2. Сильно ударить по двери ногой\n3. Осмотреть карманы в поиске чем можно вскрыть дверь\n4. Развернуться и осмотреть вашу комнату еще"
        print(options)
        choice = input("Что вы выбираете? ")
        if choice == "1":
            story = "\nВы видите коридор, напротив вашей двери еще одна дверь под номером 2"
        elif choice == "2":
            story = "\nВы сильно ударили дверь ногой, но похоже что это ни на что не повлияло."
            options = "1. Ударить еще раз!\n2. Перестать бить дверь"
            print(story)
            print(options)
            choice = input("Что вы выбираете? ")
            if choice == "1":
                story = "\nВы сильно ударили дверь ногой, но похоже что это ни на что не повлияло. Только вот теперь ваша нога болит от этого удара, так как дверь стальная"
                options = "1. Ударить еще раз!\n2. Перестать бить дверь"
                print(story)
                print(options)
                choice = input("Что вы выбираете? ")
                if choice == "1":
                    story = "\nВы очень упертый, и вы продолжаете бить эту дверь, но так и ничего не добились этим действием."
                    options = "1. Ударить еще раз! Да посильней!\n2. Перестать бить дверь"
                    print(story)
                    print(options)
                    choice = input("Что вы выбираете? ")
                    if choice == "1":
                        story = "\nВы так и продожаете бить эту несчастную дверь, может хватит это делать? Это же ведь бесполезно"
                        options = "1. ДА!!11!! БИТЬ ДАЛЬШЕ НАХ ЭТУ ДВЕРЬ!!11!!\n2. Перестать бить дверь"
                        print(story)
                        print(options)
                        choice = input("Что вы выбираете? ")
                        if choice == "1":
                            story = "\nПохоже у вас умственная отсталость, раз вы до сих пор бьете эту дверь."
                            options = "1. ДА!!11!! БИТЬ ДАЛЬШЕ НАХ ЭТУ ДВЕРЬ!!11!!\n2. Перестать бить дверь"
                            print(story)
                            print(options)
                            choice = input("Что вы выбираете? ")
                            if choice == "1":
                                story = "\nЧЕЛ МОЖЕТ РЕАЛЬНО ХВАТИТ БИТЬ ЭТУ ДВЕРЬ!?!? У ТЕБЯ УЖЕ ОГРОМНЫЙ СИНЯК НА НОГЕ!"
                                options = "1. НЕ ОСТАНАВЛИВАТЬСЯ! БИТЬ! БИТЬ! БИТЬ!\n2. Перестать бить дверь"
                                print(story)
                                print(options)
                                choice = input("Что вы выбираете? ")
                                if choice == "1":
                                    story = "\nЛадно! Бей дальше! Но знай, это бесполезно!"
                                    options = "1.Ударить еще! \n2. Перестать бить дверь"
                                    print(story)
                                    print(options)
                                    choice = input("Что вы выбираете? ")
                                    if choice == "1":
                                        story = "\nВы ударили еще раз, на двери уже осталась небольшая вмятина"
                                        options = "1. Ударить еще! я точно знаю что так можно пройти этот квест! \n2. Перестать бить дверь"
                                        print(story)
                                        print(options)
                                        choice = input("Что вы выбираете? ")
                                        if choice == "1":
                                            story = "\n Похоже что вы начали думать что вы находитесь в квесте, возможно это произошло из-за сильного болевого шока, так как вы сломали стопу ноги."
                                            options = "1.Я реально ябнутый! Бить дальше! Не сдаваться! \n2. Перестать бить дверь"
                                            print(story)
                                            print(options)
                                            choice = input("Что вы выбираете? ")
                                            if choice == "1":
                                                story = "\n"
                                                options = "1. \n2. Перестать бить дверь"
                                                print(story)
                                                print(options)
                                                choice = input("Что вы выбираете? ")
                                                if choice == "1":
                                                    story = "\n"
                                                    options = "1. \n2. Перестать бить дверь"
                                                    print(story)
                                                    print(options)
                                                    choice = input("Что вы выбираете? ")
                                                    if choice == "1":
                                                        story = "\n"
                                                        options = "1. \n2. Перестать бить дверь"
                                                        print(story)
                                                        print(options)
                                                        choice = input("Что вы выбираете? ")
                                                        if choice == "1":
                                                            story = "\n"
                                                            options = "1. \n2. Перестать бить дверь"
                                                            print(story)
                                                            print(options)
                                                            choice = input("Что вы выбираете? ")
                                                            if choice == "1":
                                                                story = "\n"
                                                                options = "1. \n2. Перестать бить дверь"
                                                                print(story)
                                                                print(options)
                                                                choice = input("Что вы выбираете? ")
                                                                if choice == "1":
                                                                    story = "\n"
                                                                    options = "1. \n2. Перестать бить дверь"
                                                                    print(story)
                                                                    print(options)
                                                                    choice = input("Что вы выбираете? ")
                                                                    if choice == "1":
                                                                        story = "\n"
                                                                        options = "1. \n2. Перестать бить дверь"
                                                                        print(story)
                                                                        print(options)
                                                                        choice = input("Что вы выбираете? ")
                                                                    elif choice == "2":
                                                                        continue
                                                                elif choice == "2":
                                                                    continue
                                                            elif choice == "2":
                                                                continue
                                                        elif choice == "2":
                                                            continue
                                                    elif choice == "2":
                                                        continue
                                                elif choice == "2":
                                                    continue
                                            elif choice == "2":
                                                continue
                                        elif choice == "2":
                                            continue
                                    elif choice == "2":
                                        continue
                                elif choice == "2":
                                    continue
                            elif choice == "2":
                                continue
                        elif choice == "2":
                            continue
                    elif choice == "2":
                        continue
                elif choice == "2":
                    continue
            elif choice == "2":
                continue
    elif choice == "2":
        story += "\nВы пытаетесь выбить окно, но оно прочное."
    elif choice == "3":
        story += "\nВы находите старую книгу в шкафу, но она на иностранном языке."
    elif choice == "4":
        story += "\nВы засыпаете и просыпаетесь утром. Какой странный сон!"

    # Добавьте другие варианты ответов и соответствующие изменения в истории игры здесь

    else:
        print("Выберите правильный вариант ответа!")
