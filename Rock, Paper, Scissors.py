import random
import time as t

print("Welcome to rock, paper, scissors! May the best of three win!")

t.sleep(1)

pChoice = ""
cChoice = ""

#Possible choices
rock = ["rock", "Rock", "ROCK", "r", "R"]
paper = ["paper", "Paper", "PAPER", "p", "P"]
scissors = ["scissors", "Scissors", "SCISSORS", "s", "S"]
cChoices = ["rock", "paper", "scissors"]

#Points
pPoints = 0
cPoints = 0

#Loop
while True:
  #Player choice
  while True:
    print("")
    pInput = input("Your choice: ")
    if pInput in rock:
      pChoice = "rock"
      break
    elif pInput in paper:
      pChoice = "paper"
      break
    elif pInput in scissors:
      pChoice = "scissors"
      break
    else:
      print("Invalid choice. Enter rock, paper or scissors")
  #Computer choice
  cChoice = random.choice(cChoices)
  #Choices are printed
  print("")
  t.sleep(1)
  print("You chose", pChoice)
  t.sleep(1)
  print("Computer chose", cChoice)
  #Decide the winner
  if (pChoice == "rock" and cChoice == "scissors") or (pChoice == "paper" and cChoice == "rock") or (pChoice == "scissors" and cChoice == "paper"):
    pPoints += 1
    print("")
    t.sleep(1)
    print("You won this round!")
    t.sleep(1)
    print("")
    t.sleep(1)
    print("Player points:", pPoints)
    print("Computer points:", cPoints)
    if pPoints == 3:
      break
  elif (cChoice == "rock" and pChoice == "scissors") or (cChoice == "paper" and pChoice == "rock") or (cChoice == "scissors" and pChoice == "paper"):
    cPoints += 1
    print("")
    t.sleep(1)
    print("You lost this round!")
    t.sleep(1)
    print("")
    t.sleep(1)
    print("Player points:", pPoints)
    print("Computer points:", cPoints)
    if cPoints == 3:
      break
  elif (pChoice == "rock" and cChoice == "rock") or (pChoice == "paper" and cChoice == "paper") or (pChoice == "scissors" and cChoice == "scissors"):
    print("")
    t.sleep(1)
    print("It was a tie! No one got any points.")
    t.sleep(1)
    print("")
    t.sleep(1)
    print("Player points:", pPoints)
    print("Computer points:", cPoints)

#Print out who the winner is
if pPoints == 3:
  print("")
  t.sleep(1)
  print("Congratulations! You won the game!")
elif cPoints == 3:
  print("")
  t.sleep(1)
  print("Oh no! You lost the game! Good luck next time.")