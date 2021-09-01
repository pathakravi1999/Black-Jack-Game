import random
from replit import clear

def deal_card():
  cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards)== 2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score>21 and computer_score>21:
    return "You lose"
  if user_score == computer_score:
    return "Its a draw"
  elif user_score ==0 :
    return "You win"
  elif computer_score == 0:
    return "Oops You lose Opponent has blackjack"
  elif user_score>21:
    return "You went over You lose"
  elif computer_score>21:
    return "Computer went over You win!"
  else:
    return " You lose"
def play_game():
  

  user_card=[]
  computer_card=[]
  for _ in range(2):
    user_card.append(deal_card)
    computer_card.append(deal_card)

  should_continue = True
  while should_continue:


    user_score = calculate_score(user_card)
    computer_score= calculate_score(computer_card)
    print(f"Your cards:{user_card}, current_score: {user_score}")
    print(f"Computer card{computer_card}")

    if user_score==0 or computer_score == 0 or user_score>21:
      should_continue = False
    else:
      ask = input("Type 'Y' to get another card or type 'N' to end").lower()
      if ask== "Y":
        user_card.append(deal_card)
      if ask =="N":
        should_continue = False
      
    while computer_score!=0 and computer_card<17:
      computer_card.append(deal_card)
      computer_score = calculate_score(computer_score)  
  print(f" Your cards: {user_card}, current_score {user_score}")
  print(f" Computer cards : {computer_card}, computer_score: {computer_score}")
  print(compare(user_score,computer_score))
while input("Do you want to continue playing blackjack? Type 'Y' if Yes, Type 'N' if you dont").lower() == "y":
  clear()
  play_game()







        






