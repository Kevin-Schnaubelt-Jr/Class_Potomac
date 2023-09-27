# 1 meter (m) = 3.28 feet (ft) 
# inserttime
user_unit=input("What are you mesuring in today? : ")
if user_unit=="feet":
    x = input("Give me a number in feet and ill convert it into meters! : ")
    y = int(x) * 0.30483
    print(y)
elif user_unit=="meters":
    x = input("Give me a number in meters and ill convert it into meters! : ")
    y = int(x) * 1
    print(y)
elif user_unit=="miles":
    x = input("Give me a number in meters and ill convert it into miles! : ")
    y = int(x) * 1609.34
    print(y)
elif user_unit=="kilometers":
    x = input("Give me a number in meters and ill convert it into kilometers! : ")
    y = int(x) / 1000
    print(y)
round_user=input("Do you want to round this? Y/N : ")
if round_user=="y":
    print(round(y,5))
elif round=="n":
    pass