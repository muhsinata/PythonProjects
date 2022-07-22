#Necessary functions for blackjack game

dealer_hand = random.choices(cards, k = 2)
player_hand = random.choices(cards, k = 2)
player_total = sum(player_hand)
dealer_total = sum(dealer_hand)

def dealer_possibilites1():
    """If player doesn't have blackjack, this function 
    calculates the possibilites of dealer in terms of 
    new cards added until dealer reaches 17."""
    global dealer_total
    if dealer_total < 17:
        while dealer_total < 17:
            new_card = random.choice(cards)
            dealer_hand.append(new_card)
            dealer_total += new_card
            print(f"Dealer Hand\n{dealer_hand}. Total: {dealer_total}\n")
        if dealer_total > 21:
            print("PLAYER WIN!")
        elif dealer_total == 21:
            print("DEALER WIN!")
            keep_hitting = False
        else:
            if dealer_total > player_total:
                print("DEALER WIN!")
                keep_hitting = False
            elif dealer_total == player_total:
                print("PUSH!")
                keep_hitting = False    
            else:
                print("PLAYER WIN!")
                keep_hitting = False
    else:
        if dealer_total > player_total:
            print("DEALER WIN!")
            keep_hitting = False
        elif dealer_total == player_total:
            print("PUSH!")
            keep_hitting = False    
        else:
            print("PLAYER WIN!")
            keep_hitting = False 

def dealer_possibilites2():
    """If player has a blackjack, this function 
    calculates the possibilites of dealer in terms of 
    new cards added until dealer reaches 17."""
    global dealer_total
    print("PLAYER BLACKJACK!\n")
    print(f"Dealer Hand\n{dealer_hand}. Total: {dealer_total}\n")
    if dealer_total < 17:
        while dealer_total < 17:
            new_card = random.choice(cards)
            dealer_hand.append(new_card)
            dealer_total += new_card
            print(f"Dealer Hand\n{dealer_hand}. Total: {dealer_total}\n")
        if dealer_total == 21:
            print("PUSH!")
            keep_hitting = False
        else:
            print("PLAYER WIN!")
            keep_hitting = False
    elif dealer_total == 21:
        print(f"Dealer Hand\n{dealer_hand}. Total: {dealer_total}\n")
        print("PUSH!")
        keep_hitting = False
    else:
        print("PLAYER WIN!")
        keep_hitting = False

