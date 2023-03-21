import numexpr
def calc(a, b, operator):
    print(numexpr.evaluate(str(a + operator + b)))
a = input("Число A: ")
b = input("Число B: ")
operator = str(input("математический оператор: "))
calc(a, b, operator)