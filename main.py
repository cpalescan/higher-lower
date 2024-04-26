## import libraries
from art import logo
from art import vs
from game_data import data
import random


## pick a random dictionary from data (list) and generate variables with the values. 
## Store "follower_count"

def picker():
  """Picks a random dictionary from the list. Prints name, description and country. 
  Stores follower count"""
  random_number = random.randint(0, len(data) - 1)
  chosen = data[random_number]
  name = chosen["name"]
  followers = chosen["follower_count"]
  description = chosen["description"]
  country = chosen["country"]
  print(f"{name}, a {description} from: {country}")
  return followers

## user input
def user_choice():
  """Asks for the input. Transforms the input into a choice between the variables a and b."""
  user = input("Who has more followers? Pick 'A' or 'B':   ").lower()
  if user != "a" and user != "b":
    user = input("Please type 'A' or 'B':    ").lower()
  elif user == "a":
    other = b
    return a
  elif user == "b":
    other = a
    return b

## compare data
def check(picked_by_user, other_one):
  """ Compares answers, adds points to score. Eventually ends the game."""
  if picked_by_user > other_one:
    print("Good guess")
    print("")
    print("")
    global score
    score += 1
    return False
    
  elif picked_by_user < other_one:
    print("Oh no, wrong answer!")
    return True
    
    

## starting conditions
  
game_over = False
score = 0


## body
print(logo)
print("")
print("")
print("")
while game_over == False:

    
  a = picker()
  print("")
  print(vs)
  print("")
  b = picker()
  if b == a:
    b = picker()
    
  chosen_one = user_choice()
  if chosen_one == a:
    other = b
  elif chosen_one == b:
    other = a
  
  game_over = check(chosen_one, other)



print(f"Your final score is {score}")



    
    
  