import random
import time
specialcases={
    "0":"zero",
    "10":"ten",
    "11":"elevin",
    "12":"twelve",
    "13":"thirteen",
    "14":"fourteen",
    "15":"fifteen",
    "16":"sixteen",
    "17":"seventeen",
    "18":"eighteen",
    "19":"nineteen"
}
tens={
    "20":"twenty",
    "30":"thirty",
    "40":"fourty",
    "50":"fifty",
    "60":"sixty",
    "70":"seventy",
    "80":"eighty",
    "90":"ninty"
}
bases={
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
    "0" : ""
}
def convert(inputtext):
    toconv = str(inputtext)
    length = len(toconv)
    if toconv in specialcases:
        print(specialcases[toconv])
    elif length == 1:
        return bases[toconv]
    elif length == 2 and toconv[1] != "0":
        return f"{tens[toconv[0]+'0']}-{bases[toconv[1]]}"
    elif length == 2 and toconv[1] == "0":
        return tens[toconv[0]+'0']
    elif length == 3 and toconv[1]!="0"and toconv[2]!=0:
        return f"{bases[toconv[0]]}-hundred-{convert(toconv[1]+toconv[2])}"
    elif length == 3 and toconv[1]=="0"and toconv[2]!=0:
        return f"{bases[toconv[0]]}-hundred-and-{convert(toconv[2])}"
    elif length == 3 and toconv[1]!="0"and toconv[2]==0:
        return f"{bases[toconv[0]]}-hundred-{convert(toconv[1]+'0')}"

print("Welcome To:")
print('''
  _____ _____ _____ _  __   _____ _______   __
 |  __ \_   _/ ____| |/ /  / ____|_   _\ \ / /
 | |__) || || |    | ' /  | (___   | |  \ V / 
 |  ___/ | || |    |  <    \___ \  | |   > <  
 | |    _| || |____| . \   ____) |_| |_ / . \ 
 |_|   |_____\_____|_|\_\ |_____/|_____/_/ \_\\
                                              
                                              
      ''')

winning_numbers=[]
for x in range(6):
    winning_numbers.append(random.randint(0,9))
while True:
    matches = 0
    ticket1 = int(input("Enter Number One!\n>>> "))
    ticket2 = int(input("Enter Number Two!\n>>> "))
    ticket3 = int(input("Enter Number Three!\n>>> "))
    ticket4 = int(input("Enter Number Four!\n>>> "))
    ticket5 = int(input("Enter Number Five!\n>>> "))
    ticket6 = int(input("Enter Number S I X!\n>>> "))
    
    print("Calculaiting Numbers...")
    newrand1 = random.randint(1,99)
    newrand2 = random.randint(1,99)
    newrand3 = random.randint(1,99)
    newrand4 = random.randint(1,99)
    newrand5 = random.randint(1,99)
    newrand6 = random.randint(1,99)
    
    print(f"{ticket1} - {newrand1}")
    print(f"{ticket2} - {newrand2}")
    print(f"{ticket3} - {newrand3}")
    print(f"{ticket4} - {newrand4}")
    print(f"{ticket5} - {newrand5}")
    print(f"{ticket6} - {newrand6}")

    if ticket1 == newrand1:
        matches += 1
    if ticket2 == newrand2:
        matches += 1
    if ticket3 == newrand3:
        matches += 1
    if ticket4 == newrand4:
        matches += 1
    if ticket5 == newrand5:
        matches += 1
    if ticket6 == newrand6:
        matches += 1
    print(f"You Got {matches} Matches!")