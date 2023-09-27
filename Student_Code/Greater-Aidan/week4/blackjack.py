import random

# Define the deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

# Assign values to cards
card_values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
               'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

def create_deck():
    return [{'Rank': rank, 'Suit': suit, 'Value': card_values[rank]} for suit in suits for rank in ranks]

# Function to calculate the total value of a hand
def calculate_hand_value(hand):
    total_value = sum(card['Value'] for card in hand)
    num_aces = sum(1 for card in hand if card['Rank'] == 'Ace')

    # Handle Aces as 1 or 11
    while total_value > 21 and num_aces > 0:
        total_value -= 10
        num_aces -= 1

    return total_value

# Function to display a player's hand
def display_hand(hand):
    for card in hand:
        print(f"{card['Rank']} of {card['Suit']}")

# Function to display advice based on hand value
def display_advice(hand_value):
    if hand_value < 17:
        print("Advice: You should 'hit'.")
    else:
        print("Advice: You should 'stand'.")

# Initialize credits
credits = 10

while True:
    # Check if the player has enough credits to play
    if credits < 1:
        print("You don't have enough credits to play.")
        break

    # Deduct 1 credit for playing
    credits -= 1

    # Create a new deck and shuffle it
    deck = create_deck()
    random.shuffle(deck)

    # Initialize the player and dealer hands
    player_hand = []
    dealer_hand = []

    # Deal the initial cards
    for _ in range(2):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())

    # Game loop
    while True:
        player_total = calculate_hand_value(player_hand)
        dealer_total = calculate_hand_value(dealer_hand)

        # Display hands and advice
        print("\nYour hand:")
        display_hand(player_hand)
        print(f"Total value: {player_total}")
        display_advice(player_total)
        print("\nDealer's hand:")
        print(f"{dealer_hand[0]['Rank']} of {dealer_hand[0]['Suit']}")
        print("Total value: ?\n")

        # Check for player Blackjack or bust
        if player_total == 21:
            print("Blackjack! You win!")
            credits += 2
            break
        elif player_total > 21:
            print("Bust! You lose.")
            break

        # Ask the player to hit or stand
        action = input("Do you want to 'hit' or 'stand'? ").strip().lower()
        if action == 'hit':
            card = deck.pop()
            if card['Rank'] == 'Ace':
                ace_value = input("Do you want the Ace to be worth 1 or 11? ").strip()
                card['Value'] = int(ace_value)
            player_hand.append(card)
        elif action == 'stand':
            # Dealer's turn
            while dealer_total < 17:
                dealer_hand.append(deck.pop())
                dealer_total = calculate_hand_value(dealer_hand)

            # Display the dealer's hand
            print("\nDealer's hand:")
            display_hand(dealer_hand)
            print(f"Total value: {dealer_total}\n")

            # Determine the winner
            if dealer_total > 21 or player_total > dealer_total:
                print("You win!")
                credits += 2
            elif dealer_total > player_total:
                print("Dealer wins.")
            else:
                print("It's a tie!")

            break
        else:
            print("Invalid input. Please enter 'hit' or 'stand'.")

    print(f"Your remaining credits: {credits}")
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        break
