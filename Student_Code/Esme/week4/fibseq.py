z = 0
x = 0
y = 1
while z < 255:
    z = x+y
    y = x
    x = z
    print(z)
    