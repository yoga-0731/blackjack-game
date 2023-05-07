import random
from art import logo
from cards import cards
from replit import clear

def get_card(cards):
  return random.choice(cards)

def get_sum(game_cards):
  sum = 0
  for num in game_cards:
    sum += num
  return sum

def player_game(player_cards):
  card = get_card(cards)
  return card

def computer_game(computer_cards):
  computer_cards.append(get_card(cards))
  print(f"\nComputer's final hand: {computer_cards}")
  return sum(computer_cards)

# Compare scores while taking cards
def print_result(player_cards, computer_cards, score):
  if score == 21:
    print("BlackJack - You Win!")
    return True
  elif score > 21:
      print("You lose")
      return True
  return False

# Display Scores
def display_score(result, player_sum, comp_sum):
  if result == False:
    print(f"\n\nPlayer score: {player_sum}\nComputer score: {comp_sum}\n")
    if player_sum == comp_sum:
      print("Draw!")
    elif comp_sum == 21:
      print("You lose")
    elif player_sum > comp_sum or comp_sum > 21:
      print("You Win!!")
    else:
      print("You lose")

# Play game
def play():

  print(logo + "\n\n")

  # Get cards
  player_cards = random.choices(cards, k = 2)
  play_sum = sum(player_cards)
  print(f"Player cards: {player_cards}, Current Score: {play_sum}")
  computer_cards = random.choices(cards, k = 2)
  print(f"Computer's first card: {computer_cards[0]}")

  result = print_result(player_cards, computer_cards, sum(player_cards))

  if result == False:
    # Calculate Score
    continue_game = input("Type 'y' to get another card or 'n' to hold: ")
    player_sum = play_sum

    while continue_game == 'y' and result == False:
      card = player_game(player_cards)
      player_cards.append(card)
      player_sum += card
      if 11 in player_cards:
        player_cards.remove(11)
        player_cards.append(1)
      player_sum = sum(player_cards)
      print(f"\n\nPlayer cards: {player_cards}, Current Score: {player_sum}\n")
      result = print_result(player_cards, computer_cards, player_sum)
      if result == False:
        continue_game = input("Type 'y' to get another card or 'n' to hold: ")
    comp_sum = computer_game(computer_cards)
    display_score(result, player_sum, comp_sum)


continue_game =  True

while continue_game:
  play_game = input("Do you want to play BlackJack game? Type 'y' or 'n': ")
  if play_game == 'y':
    play()
    continue_playing = input("Do you want to restart game 'y' or 'n': ")
    if continue_playing == 'y':
      clear()
  else:
    continue_game = False


