import random

randomtonine = [1,2,3,4,5,6,7,8,9]
balance = 0
numlist = [1,1,1,1,1,1]
yournumlist = [random.choice(randomtonine),random.choice(randomtonine),random.choice(randomtonine),random.choice(randomtonine),random.choice(randomtonine),random.choice(randomtonine)]
balance = 0
matching = 0
looper = 0
count = 0
moneyspent = 0
moneygained = 0
print(numlist)
choice = input("whould you like to buy 100,000 lottery tickets they are 2$ (y/n)")
if choice == "yes":
    looper = 1000000
    while looper >0:
        balance -= 2
        moneyspent += 2
        for x in numlist:
            # print(type(x), "this is x")
            # print("num at count", type(yournumlist[count]))
            if x == yournumlist[count]:
                matching +=1
                #print("matching", matching)
            count += 1
        if matching == 1:
            balance +=4
            moneygained +=4
        elif matching == 2:
            balance +=7
            moneygained +=7
        elif matching == 3:
            balance +=100
            moneygained +=100
        elif matching == 4:
            balance += 50000
            moneygained +=50000
        elif matching == 4:
            balance += 1000000
            moneygained +=1000000
        elif matching == 4:
            balance += 25000000
            moneygained +=25000000
        count = 0
        yournumlist = [random.choice(randomtonine),random.choice(randomtonine),random.choice(randomtonine),random.choice(randomtonine),random.choice(randomtonine),random.choice(randomtonine)]
        looper -= 1
    #print(f"matching = {matching}")
    print(f"money lost:{moneyspent}")
    print(f"money gained:{moneygained}")
    print(f"your balance is:{balance}")
    print(f"your numbers are:{yournumlist}")
