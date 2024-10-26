from random import choice

cards = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,'8': 8,'9': 9, '10':10, 'J':10, 'Q':10, 'K':10}

player_cards = []
computer_cards = []

def deal_card():
  for i in range(5):
    player_cards.append(choice(list(cards.keys())))
    computer_cards.append(choice(list(cards.keys())))
deal_card()

def computer_score(computer_cards=computer_cards[0]):
  comp_score=sum([cards[i] for i in computer_cards])
  return int(comp_score)

def player_score(player_cards=player_cards[0:2]):
  player_score=sum([cards[i] for i in player_cards])
  return int(player_score)

playerScore=player_score()
computerScore=computer_score()


# Game Start
def printer(playerCards=player_cards[0:2], computerCards=computer_cards[0]):
    print(f'Player cards: {playerCards} \t Score: {player_score(playerCards)}')
    print(f'Computer cards: {computerCards} \t Score:  {computer_score(computerCards)}')
printer()

# def A_checker():
#     if 'A' in player_cards and player_score()>21:

m=2
while computerScore<17:
    computerScore=computer_score((computer_cards[0:m]))
    m+=1


if player_score() > 21:
    print("You lose")
elif player_score() == 21:
    print("You win")
elif player_score() < 21:
    action=input("Do you want to hit or stand?\n").lower()
    if action == "stand":
       printer(player_cards[0:2], computer_cards[0:m-1])    
       if player_score(player_cards[0:2])> computerScore:
           print("You win")
       else:
           print("You lose")
    elif action == "hit":
       while action == "hit":
          i=3
          printer(player_cards[0:i], computer_cards[0:m-1])
          i+=1
          if player_score(player_cards[0:i])> 21:
             print("You lose")
             break
          elif player_score(player_cards[0:i])== 21:
             print("You win")
             break
          elif player_score(player_cards[0:i])< 21:
             action=input("Do you want to hit or stand?\n").lower()
             if action == "stand":
                printer(player_cards[0:i], computer_cards[0:m-1])
                if player_score(player_cards[0:i])> computerScore:
                   print("You win")
                else:
                    print("You lose")

'''I have to deal with rendering 11 when necessary and 1 when necessary
   since we capped comp_score at index0 score calcutlation by loop is getting issues from time to time
   I also have to code the computer session so that it adds extra cards when below 17
'''