score = 0
for i in range(1, 3):
    primer = "5+6*" + str(i) + "="
    human = input(primer)
    if int(human) == 5+6*i:
        score+=1
print("счет =",score)