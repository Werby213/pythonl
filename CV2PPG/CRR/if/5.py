usd = 60.55
eur = 62.74
rub = float(input(("Рублей: ")))
type = str(input(("На что меняем: ")))
if type == "USD":
    print ("$" , rub / usd)
elif type == "EUR":
    print(rub / eur , "€")