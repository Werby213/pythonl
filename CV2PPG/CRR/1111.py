def decimal_to_binary(decimal_number):
    binary_number = ""

    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number = decimal_number // 2

    return binary_number

decimal_number = int(input("Введите десятичное число: "))
binary_number = decimal_to_binary(decimal_number)

print("Двоичное число: ", binary_number)
