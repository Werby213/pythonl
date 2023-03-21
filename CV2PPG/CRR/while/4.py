spisok = [1, 2]
active = True
i = 2
while active:
    n=input("quit: ")
    if n=="quit":
        active = False
    i = i + 1
    spisok.append(i)
    print(spisok)