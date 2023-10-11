import random

money = 100
        
def pick_six():
    counter=0
    return_number=[]
    while counter<6:
        return_number.append(random.randint(0,25))
        counter += 1
    return return_number

winnings = {
    0:0,
    1:4,
    2:7,
    3:100,
    4:50000,
    5:1000000,
    6:25000000
}

w = pick_six()
p = pick_six()

print(w)
print(p)

counter=0
matches=0

for number in p:
    if number==w[counter]:
        matches+=1
    counter+=1

print(winnings[matches]) 
