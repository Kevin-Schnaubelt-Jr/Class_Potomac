def Cleanlist(LISTUSE):
    returnlist = ""
    for i in LISTUSE:
        returnlist = returnlist + i + ", "
    return returnlist[:-2] + "."
foods=[]
while True:
    newfood = input("Enter A Food:\n>>>")
    foods.append(newfood)
    newfood = input("Would You Like To Continue?\n(Y/N)\n>>>").upper()
    if newfood != "Y":
        break
print(Cleanlist(foods))
