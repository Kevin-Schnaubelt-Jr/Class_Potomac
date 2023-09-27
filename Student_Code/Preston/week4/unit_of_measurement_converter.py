#1ft = 0.3048m
#round(x,place to round to)
#1mi = 1609.34m
#m=m
#1km = 1000m
m = input("""choose
          feet
          miles
          meters
          kilometers
          
          """)
num = input("choose how many to convert")
e = input("choose what to convert it to")

def numtometers(m,feet,mile,meters,kilometers):
    if m == "feet":
        returnn = feet
    elif m == "mile":
        returnn = mile
    elif m == "meters":
        returnn = meters
    elif m == "kilometers":
        returnn = kilometers
    print(returnn, type(returnn))
    return int(returnn)
def mtoelse(mtofeet,mtomile,mtokilometers):
    if e == "feet":
        returne = mtofeet
    elif e == "mile":
        returne = mtomile
    elif e == "kilometers":
        returne = mtokilometers
    elif e == "meters":
        returne = e
    return returne

feet = round(int(num)*0.3048,2)
mile = round(int(num)*1609.34,2)
meters = m
kilometers = round(int(num)*1000,2)

ntm =numtometers(m,feet,mile,meters,kilometers)
print(ntm)
print(type(ntm))

mtofeet = round(int(ntm)/0.3048,2)
mtomile = round(int(ntm)/1609.34,2)
mtokilometers = round(int(ntm)/1000,2)

mte = mtoelse(ntm,mtofeet,mtomile,mtokilometers)

print(f"""you chose to convert {num} {m} to {e} you got {mte}""")
