import random
import time

# card1 = input("whats your first card ")
# card2 = input("whats your second card ")
# card3 = input("whats your third card ")

# cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
# card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# sum_of_cards = card_values[card1] + card_values[card2] + card_values[card3]
# if sum_of_cards <17:
#     print("You should hit")
# elif sum_of_cards >21:
#     print("You Busted!")
# elif sum_of_cards <17:
#     print("Avoid hitting")

random_card = random.choice(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'])
random_card1 = random.choice(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'])
random_card2 = random.choice(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'])
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

sum_of_cards = card_values[random_card] + card_values[random_card1] + card_values[random_card2]

print (f"Your first two cards are {random_card} and {random_card2}")
hit = input("Do you want to hit (y/n) ")
if hit == "y":
    print(f"Your second card is {random_card1}")
    if sum_of_cards>21:
        print("You busted!")
    if sum_of_cards<21:
        hit2 = input("Do you want to hit? ")
        if hit2 == "y":
            print (f"Your card is {random_card2} ")
        if sum_of_cards>21:
                print("You busted! ")
        if sum_of_cards<21:
            hit3 = ("Do you want to hit?")
            if hit3 == "y":
                print(f"Your card is {random_card2}")

    