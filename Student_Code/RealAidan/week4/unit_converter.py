# 1ft=0.3048m
# 1mi=160.34m
# km=1000m
import time
ask=input("Are you converting feet, miles, or kilometer ")
while True:

    user_number=input(f"Enter number in {ask} to get number in meters? ")
    if ask==("feet"):
        ans= int(user_number)*0.3048
        number=round(ans,1)
    elif ask==("miles"):
        ans= int(user_number)*160.34
        number=round(ans,1)
    elif ask==("kilometer"):
        ans= int(user_number)*1000
        number=round(ans,1)
    time.sleep(1.5)
    print(number)
    again=input("Do you want to convert another ")
    if again != "yes":
        break