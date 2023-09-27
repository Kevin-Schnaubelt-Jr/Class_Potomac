specifcards={
    "jack":10,
    "queen":10,
    "king":10
}

cards = []

looper = True
while looper:

    playerscard = input("what is one of your cards")
    cards.append(playerscard)
    continuee = input("do you have any more cards?")
    if continuee == "no":
        looper = False
cardssum = 0
result = ""
ace = ""
for x in cards:
    if x in specifcards:
         cardssum += 10
    elif x == int:
        cardssum += int(x)
for x in cards:
    if x == "ace":
        if cardssum <=6:
            cardssum += 11
            ace = "/ace should be 11"
        else:
            cardssum += 1
            ace = "/ace should be 1"
if cardssum < 17:
    result = "add"
elif cardssum >=17 and cardssum <21:
    result = "stay"
elif cardssum == 21:
    result = "you won"
elif cardssum >21:
    result = "you lost"

print (result,ace)