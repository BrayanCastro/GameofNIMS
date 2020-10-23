# Author: Brayan Castro Lugo
# Program: Nims Rumble
# Description: This program runs a game in which there are two players who begin with a pile of 21 stones. Each player take turns. 
#  Each turn, a player may take either one, two or three stones. They must take at least one stone, and cannot take more than three stones. The player who takes the final stone loses the game


#Step 1: Is the game over?
#This function takes a number of stones as input and returns True if and only if the game is over
#Parameters: stones, the current number of stones remaining in the pile 
#Returns: True if zero stones remain, False otherwise

def is_game_over(stones):
  if stones == 0:
    return True
  else:
    return False
  
  
#Step 2: Who is the next player?  
#This function takes in the current player's name and returns the next players name.
#Parameter: currentPlayer, a string representing who is currently taking a turn 
#Returns: the next player

def next_player(currentPlayer):
    if currentPlayer == 'Tony':
        return "Leroy"
    else:
        return "Tony"
      
           
#Step 3: How many stones do you want to take?
#This functionasks how many stones a player wants to take. The player must take at least one stone and can take at most three, but cannot take more stones than are left. If the user enters an invalid number of stones, a helpful error message appears and ask the user again.
#Parameter: currentPlayer, the name of the player whose turn it is
#Parameter: stones, the number of remaining stones
#Returns: the number of stones the player chose to take

def get_choice (currentPlayer, stones):
  print(currentPlayer+", it is your turn.")
  while True:
    picked_stones =int(input("There are {} stones left. How many stones will you take?".format(stones)))
    if picked_stones < 1:
      print(currentPlayer, "you must take at least one stone.")
      continue
    elif picked_stones > 3:
      print(currentPlayer, "you cannot take more than 3 stones.")
      continue
    elif picked_stones > stones:
      print(currentPlayer, "you cannot take more than", stones ,"stones.")
      continue
    else:
      return picked_stones
    
    
#Step 4: Putting it all together   
#This is the main function which implements a game loop. 
#The game loop should quit when is_game_over returns True. Each turn, the current player should choose a legal number of stones. Those stones are to be removed from the pile of remaining stones, and the current player should be updated using next_player.

def main():
  print("Welcome to Rhodes Rumbles!")
  stones=21
  currentPlayer= "Leroy"
  
  while is_game_over(stones)==False:
    choice=get_choice (currentPlayer, stones)  
    currentPlayer=next_player(currentPlayer)
    stones=stones-choice
    print("")
  if is_game_over(stones) ==True:
    print("No more stones remain!")
    currentPlayer=next_player(currentPlayer)
    print (currentPlayer , "took the last stone.", currentPlayer ,"LOST" )
    currentPlayer=next_player(currentPlayer)
    print( currentPlayer, "wins.", currentPlayer, "is the AWESOMEST")
main()
 

