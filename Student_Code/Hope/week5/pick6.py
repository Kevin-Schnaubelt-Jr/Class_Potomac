import random
def pick6():
    random_list=[]
    for x in range (6):
        random_list.append(random.randint(0,9))
    return random_list



winning_number=pick6()
players_numbers=pick6()
 
# print(winning_number,players_numbers 
winning_table={
    0:0,
    1:4,
    2:7,
    3:100,
    4:50000,
    5:1000000,
    6:25000000
}
wallet=100

matches=2
i=0
for x in players_numbers:
    if x== winning_number[i]:
        matches+=1
        i+=1 
wallet-=2
wallet+=winning_table[matches]

print('winnings numbers', winning_number)
print('players numbers', players_numbers)
print(wallet, type(wallet))