import random

cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'T']
actions = ['S', 'H']

def draw_card():
    card = random.choice(cards)
    value = 11 if card == 'T' else int(card)
    return card, value

def player_turn():
    hand = []
    total = 0
    for _ in range(2):
        card, value = draw_card()
        hand.append(card)
        total += value
    return hand, total

def dealer_turn():
    hand = []
    total = 0
    for _ in range(2):
        card, value = draw_card()
        hand.append(card)
        total += value
    return hand, total

def dealer_action(hand, total):
    if total < 13:
        print('Dealer: I hit')
        card, value = draw_card()
        hand.append(card)
        total += value
    else:
        print('Dealer: I pass')
    return hand, total

def print_status(player_hand, player_total, dealer_hand, dealer_total):
    print(f"Player: {player_total}")
    print(player_hand)
    print(f"Dealer sum: {dealer_total}")
    print(dealer_hand)

def main():
    player_hand, player_total = player_turn()
    dealer_hand, dealer_total = dealer_turn()

    print_status(player_hand, player_total, dealer_hand, dealer_total)

    action = random.choice(actions)
    if action == 'S':
        dealer_hand, dealer_total = dealer_action(dealer_hand, dealer_total)
        print_status(player_hand, player_total, dealer_hand, dealer_total)
        if player_total > dealer_total or dealer_total > 21:
            print('You win')
        elif player_total <= dealer_total or player_total > 21:
            print('Dealer wins')
    else:
        card, value = draw_card()
        dealer_hand.append(card)
        dealer_total += value
        print_status(player_hand, player_total, dealer_hand, dealer_total)

if __name__ == "__main__":
    main()
