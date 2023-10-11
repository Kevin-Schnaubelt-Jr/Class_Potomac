import time

foods = []

while True:

    time.sleep(.5)
    x = input("What is your favorite food? ")
    time.sleep(.5)
    foods.append(x)
    
    

    again = input("Any other foods? y/n ")
    if again != "y":
        break

   
for food in foods:
    time.sleep(.5)
    print (food)
    time.sleep(.5)