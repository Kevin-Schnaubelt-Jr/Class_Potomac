num1=0
num2=1
old1=0
looper = 100
while num2<255:
    print(num1)
    print(num2)
    old1=num1
    num1 = num2
    num2 = old1+num2
print("done")