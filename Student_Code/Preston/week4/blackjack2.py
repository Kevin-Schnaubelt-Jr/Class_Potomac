import random

cards={
    1:1,
    2:2,
    3:3,
    4:4,
    5:5,
    6:6,
    7:7,
    8:8,
    9:9,
    10:10,
    11:11,
    12:12,
    "queen":10,
    "king":10,
    "jack":10,
}
givencard = random.choice(cards)
print(f"you got a {givencard}")