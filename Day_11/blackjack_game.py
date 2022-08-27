import random

CARDS = [2,4,5,6,7,8,9,10,10,10,10,11]


def cal_cards(card):
    if sum(card)==0 and len(card)==2:
        return 0
    if 11 in card and sum(card)>21:
        card.remove(11)
        card.append(11)
    return sum(card)

def compare(user_score,comp_score):
    if user_score>21 and comp_score>21:
        return "You went over. You lose"

    if user_score == comp_score:
        return "Draw"
    elif comp_score == 0:
        return "Lose, Opponent has Blackjact"
    elif user_score == 0:
        return "Win with BlackJack"
    elif user_score > 21:
        return "You went over, You lose"
    elif comp_score > 21:
        return "Opponent went over, You win"
    elif user_score > comp_score:
        return "You win"
    else:
        return "You lose"

def game():
    user_cards = random.choices(CARDS,k=2)
    comp_cards = random.choices(CARDS, k=2)
    is_game_over = False

    while not is_game_over:
        user_score = cal_cards(user_cards)
        comp_score = cal_cards(comp_cards)
        print(f"Your cards: {user_cards},current score: {user_score}")
        print(f"Computer cards: {comp_cards[0]}")
        
        if user_score == 0 or comp_score == 0 or user_score > 21 or comp_score > 21:
            is_game_over = True
        else:
            user_another_card = input("Do you want another card? Type 'y' or 'n': ").lower()
            if user_another_card == "y":
                user_cards.append(random.choice(CARDS))
            else:
                is_game_over = True
    
    while comp_score !=0 and comp_score <=17:
        comp_cards.append(random.choice(CARDS))
        comp_score = cal_cards(comp_cards)
    
    print(f"User cards: {user_cards},final score: {user_score}")
    print(f"Computer cards: {comp_cards}, final score: {comp_score}")
    print(compare(user_score,comp_score))

while input("Do you want to play Blackjack Game? 'y' or 'n': ").lower() == 'y':
    game()
