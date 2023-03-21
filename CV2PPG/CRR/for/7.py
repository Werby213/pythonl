inp = input()
for i in range(1, 11):
    if inp == "нечетное":
        if i % 2 == 1:
            continue
    elif inp == "четное":
            if i % 2 == 0:
                continue
        for j in range(1, 11):
            if inp == "нечетное":
                if j % 2 == 1:
                    continue
            elif inp == "четное":
                if j % 2 == 0:
                    continue
                print(i, "*",j, "=", i*j, end="\t")
            print()