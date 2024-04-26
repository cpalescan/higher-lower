## import libraries
from art import logo
from art import vs
from game_data import data
import random


## pick a random dictionary from data (list) and generate variables with the values. 
## Store "follower_count"

def picker(random_number):
  """Picks a random dictionary from the list. Prints name, description and country. 
  Stores follower count"""
  chosen = data[random_number]
  name = chosen["name"]
  followers = chosen["follower_count"]
  description = chosen["description"]
  country = chosen["country"]
  print(f"{name}, a {description} from: {country}")
  set = [name, description, country, followers, random_number]
  return(set)

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

print(logo)

## define A
random_number = random.randint(0, len(data) - 1)
set_a = picker(random_number)
a = set_a[3]

print(vs)

## define B (!= a)
random_number = random.randint(0, len(data) - 1)
while random_number == set_a[4]:
  random_number = random.randint(0, len(data) - 1)
set_b = picker(random_number)
b = set_b[3]


## body
  
while game_over == False:    
## user choice
  chosen_one = user_choice()
  if chosen_one == a:
    other = b
    chosen_set = set_a
  elif chosen_one == b:
    other = a
    chosen_set = set_b

## checking the answer
  game_over = check(chosen_one, other)

## replacing A with the right answer and generating a new B
  if game_over == False:
  
    a = chosen_one
    set_a = chosen_set
    print(f"{set_a[0]}, a {set_a[1]} from: {set_a[2]}")
    
    random_number = random.randint(0, len(data) - 1)
    while random_number == set_a[4]:
      random_number = random.randint(0, len(data) - 1)
    set_b = picker(random_number)
    b = set_b[3]
   
  
## end

print(f"Your final score is {score}")



    
    
  