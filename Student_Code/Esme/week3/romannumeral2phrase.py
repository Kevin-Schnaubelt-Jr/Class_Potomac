userinput = input("Enter A Roman Numeral\n>>> ").upper() 
romannumerals={
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}
rereturn = 0
currentnum = 0
onnum = -1
lastnum = 0
for i in userinput:
    onnum += 1 
    currentnum = romannumerals[userinput[onnum]]
    if i == 1:
        rereturn = currentnum
    else:
        if currentnum > lastnum:
            rereturn = currentnum - rereturn
        else:
            rereturn = rereturn + currentnum
    lastnum = currentnum
print(rereturn)