test = float("inf")
def int_to_roman(num):
    val = [
        1000000, 500000, 100000, 50000, 10000, 5000,
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "‾M","‾D","‾C","‾L","‾X","‾V",
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_numeral = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_numeral += syms[i]
            num -= val[i]
        i += 1
    return roman_numeral

try:
    user_input = int(input("Enter a number to be converted up to 9999999 "))
    if 0 <= user_input <= 9999999:
        roman_numeral = int_to_roman(user_input)
        print(f"The Roman numeral form of {user_input} is {roman_numeral}")
    else:
        print("enter a number between 0 and 9999999.")
except ValueError:
    print("invalid input. enter a number between 0 and 9999999.")
