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
numberrequest=input("Enter A Number\n>>> ")
def convert(toconv):
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
print(convert(numberrequest))