blackjackvalues={
    "A":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "10":10,
    "J":10,
    "Q":10,
    "K":10,
}

card1=input("Input Your First Card\n>>>").upper()
card2=input("Input Your Second Card\n>>>").upper()
card3=input("Input Your Third Card\n>>>").upper()

res = blackjackvalues[card1] + blackjackvalues[card2] + blackjackvalues[card3]

print(res)
if res < 17:
    print("Hit")
elif res < 21:
    print("Stay")
elif res == 21:
    print("Blackjack!")
elif res > 21:
    print("Busted!")