#Make a two-player Rock-Paper-Scissors game.
#  (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
#  and ask if the players want to start a new game)
import random

def game(ranf,var):
  ranf = random.choice(lst)
  print("lets play Rock ... Paper... Scissors...")
  newlst = [('rock','scissors'),('paper','rock'),('scissors','paper')]
  out = (var,ranf)
  if(var != ranf):
    if out in newlst:
      print("You are the winner",var,"wins over",ranf)
    else:
      print("You loose",var,"loses to",ranf)
  else:
    print("DRAW")
  return

gamvar={'1' : 'rock','2' : 'paper', '3' : 'scissors'}
print("Rock Paper Scissors \nChoose you choice from the provided options\n",gamvar)
lst ='rock','paper','scissors'
var = input("Your choice = \n")
var =str(gamvar[var])
print("You have chosen = ",var)
ranf = ""
game(ranf,var)




