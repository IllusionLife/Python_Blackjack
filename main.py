############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import os
import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card_face = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

player_actions = [
  "stand",
  "hit",
]

status = {
  "Blackjack": 1,
  "Lost": -1,
  "Stand": 0
}

player_detail = {
"has_ace": False,
"cards": [],
"score": 0,
"wins": 0,
}

dealer_detail = {
"has_ace": False,
"cards": [],
"score": 0,
"wins": 0,
}

def has_21(player):
  """
  Returns True if the player has a score of 21, False otherwise
  """
  if player["score"] == 21:
    return True
  return False

def has_blackjack(player):
  """
  Returns True if the player has blackjack, False otherwise
  """
  if len(player["cards"]) == 2 and has_21(player):
    return True
  return False

def has_lost(player):
  """
  Returns True if the player has over 21 and adjusts value for Aces, False otherwise
  """
  if player["score"] > 21 and player["has_ace"] == True:
    player["score"] -= 10
    player["has_ace"] = False
    
  if player["score"] > 21:
    return True
  return False

def add_win(player):
  """
  Adds a win to player/dealers win counter
  """
  player["wins"] += 1

def draw_screen():
  """
  Clears screen and prints logo
  """
  os.system('cls')
  os.system('clear')
  print(art.logo)

def draw_card(player):
  """
  Draws a cards for a player.
  Function gets a random card, adds card to score and updates player dictionary.
  """
  picked_card = random.randint(1, 13)
  picked_card -= 1
  if picked_card == 0:
    player["has_ace"] = True
  player["cards"].append(card_face[picked_card])
  player["score"] += cards[picked_card]
  return card_face[picked_card]
  
def reset_game():
  """
  Clears player and dealer data, excluding wins
  """
  #Reset player stats
  player_detail["has_ace"] = False
  player_detail["cards"] = []
  player_detail["score"] = 0
  
  #Reset dealer stats 
  dealer_detail["has_ace"] = False
  dealer_detail["cards"] = []
  dealer_detail["score"] = 0

def setup_game():
  """
  Function, used to setup the game by printing the logo and dealing cards.
  """
  reset_game()
  draw_screen()
  
  #Draw initial cards to the players
  for i in range(4):
    if i % 2 == 0:
      draw_card(player_detail)
    else:
      draw_card(dealer_detail)

def display_cards():
  """
  Print game data, including one of dealer's cards and all player cards, as well as the current scores
  """
  
  print("-------------------------------------")
  print(f"Dealer has a '{dealer_detail['cards'][0]}'")
  print(f"Dealer score: {cards[card_face.index(dealer_detail['cards'][0])]}")
  print("-------------------------------------")

  print("-------------------------------------")
  player_card_print = "You have a '" + player_detail['cards'][0] + "' "
  for i in range(1, len(player_detail['cards'])):
    player_card_print = player_card_print + "and a '" + player_detail['cards'][i] + "'"
  print(player_card_print)
  print(f"Your score: {player_detail['score']}")
  print("-------------------------------------")
  print("\n")

def print_win_score():
  """
  Funtion to print win scores between player and dealer
  """
  print(f"You have {player_detail['wins']} wins and the dealer has {dealer_detail['wins']} wins")

def print_blackjack():
  """
  Prints ASCII art when player has Blackjack
  """
  print(art.blackjack)
  print("Congrats!")
  print("You Won with a Blackjack!")
  print_win_score()

def print_win():
  """
  Prints ASCII art when player wins
  """
  print(art.win)
  print("Congratulations!!!")
  print("You Won!")
  print_win_score()

def print_loss():
  """
  Prints ASCII art when player loses
  """
  print(art.loss)
  print("Sorry...")
  print("You Lost.")
  print_win_score()

def print_tie():
  """
  Prints ASCII art when player and dealer tie
  """
  print(art.tie)
  print("It's a tie.")
  print_win_score()

def hit_or_stand():
  """
  Get input from player whether they want to draw a card or stand.
  Function checks if score is 21 and asks for input, that exists in list player_actions
  """
  chosen_action = input("Would you like to hit or stand? ").lower()
  while chosen_action not in player_actions:
    print("Invalid option. Please select one of the following actions:")
    for action in player_actions:
      print(action)
    chosen_action = input()
  if chosen_action == "hit":
    drawn_card = draw_card(player_detail)
    print(">>>>>>>>>>> Drawing card <<<<<<<<<<<<")
    print(f"You drew a {drawn_card}")
    print("\n")
    if has_21(player_detail):
      return
  elif chosen_action == "stand":
    return chosen_action

def dealer_turn():
  """
  Processes dealer's turn. Dealer will draw cards until score reaches 17 or over.
  Return:
    - status["Blackjack"] - if dealer has Blackjack
    - status["Lost"] - if dealer's score >21
    - status["Stand"] - if dealer's score is >16 and <=21  
  """
  if has_blackjack(dealer_detail) == True:
    return status["Blackjack"]
  while dealer_detail["score"] < 17:
    drawn_card = draw_card(dealer_detail)
    print(">>>>>>>>>>> Drawing card <<<<<<<<<<<<")
    print(f"Dealer drew a {drawn_card}")
    print("\n")
    if has_lost(dealer_detail):
      return status["Lost"]
  return status["Stand"]
  
def player_turn():
  """
  Processes Player's turn. Player will be asked for action.
  Return:
    - status["Blackjack"] - if dealer has Blackjack
    - status["Lost"] - if dealer's score >21
    - status["Stand"] - if dealer's score is >16 and <=21  
  """
  if has_blackjack(player_detail) == True:
    return status["Blackjack"]
  display_cards()
  while hit_or_stand() != player_actions[0]:
    if has_lost(player_detail):
      return status["Lost"]
    display_cards()
    if has_21(player_detail):
      return status["Stand"]
  draw_screen()
  display_cards()
  return status["Stand"]

def run_game():
  """
  Process game. Function will run player_turn() and dealer_turn() and calculate the game outcome.
  Will call print_win(), print_loss() or print_blackjack() and add a win point to the winner (if there is any).
  """
  result_player = player_turn()
  if result_player == status["Lost"]:
    print(f"Player has {player_detail['cards']} with a score of {player_detail['score']}")
    print(f"Dealer has {dealer_detail['cards']} with a score of {dealer_detail['score']}")
    add_win(dealer_detail)
    print_loss()
    return
  elif result_player == status["Blackjack"] and has_blackjack(dealer_detail) == False:
    print(f"Player has {player_detail['cards']} with a score of {player_detail['score']}")
    print(f"Dealer has {dealer_detail['cards']} with a score of {dealer_detail['score']}")
    add_win(player_detail)
    print_blackjack()
    return
  
  result_dealer = dealer_turn()
  print(f"Player has {player_detail['cards']} with a score of {player_detail['score']}")
  print(f"Dealer has {dealer_detail['cards']} with a score of {dealer_detail['score']}")
  if result_dealer == status["Lost"]:
    add_win(player_detail)
    print_win()
    return
  
  if result_player == status["Blackjack"]:
    add_win(player_detail)
    print_blackjack()
  elif result_dealer == status["Blackjack"]:
    add_win(dealer_detail)
    print_loss()
  else:
    if player_detail["score"] > dealer_detail["score"]:
      add_win(player_detail)
      print_win()    
    elif player_detail["score"] < dealer_detail["score"]:
      add_win(dealer_detail)
      print_loss()
    else:
      print_tie()


#Main body starts here
new_game = "yes"
while new_game != "no":
  setup_game()
  run_game()
  
  new_game = input("Would you like to play another game? Yes or no: ").lower()
  while new_game != "yes" and new_game != "no":
    new_game = input("Invalid input. Please select \"Yes\" or \"No\": ").lower()
