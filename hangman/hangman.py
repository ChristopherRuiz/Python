import random

# Global Variable Declaration
game_over = 6
easy_list = ["drive","seat","stop","sled","lie"]
hard_list = ["unknown","yummy","espionage","hyphen","rhythm"]


# Easy Game of Hangman
def easy_game(game_list):
  # Some variable declarations for the easy_game function
  guess_count = 0
  game_word = easy_list[random.randint(0,4)]
  word_count = len(game_word)
  word_char = list(game_word)
  guess_list = []

  # Printing out blank spaces for the letters in the word
  for i in range(word_count):
    guess_list.append("_")
    print("_", end=' ')
  print("\n")

  # While loop to iterate  until all guesses have been used(game over) or the user guesses the word correctly 
  while guess_count != game_over | word_count >= 0:
    guess = input("Enter your guess: ")  

    # If letter guessed is in the word list(word_char), then insert the value in the guess_list at the index the letter was found in the word list
    if guess.lower() in word_char:
      print("Correct!", guess.lower(), "is in the word")
      guess_list[word_char.index(guess)] = guess      

      # print out the updated game board
      for i in guess_list:
        print(i, end=' ')

      print("\n")
      word_count -= 1

      # Exit game when won
      if word_count == 0:
        print("You won!")
        break
    
    elif guess.lower() not in word_char:
      print(guess.lower(),"is not in the word")
      
      # print current guessed letters in word
      for i in guess_list:
        print(i, end=' ')
      print("\n")
      guess_count += 1

      # Exit game when lost
      if guess_count == 6:
        print("You Lost...")
        break

        


# Hard Game of Hangman
def hard_game(game_list):
  for i in game_list:
    print(i)

# Start the game
def game_start():
  print("==============================")
  print("      WELCOME TO HANGMAN      ")
  print("==============================")

  while True:
    choice = input("Choose your difficulty level: \n1. Easy \n2. Hard\n")

    #Try to convert user input into integer, and catch any input that is not an integer
    #If input was anything but an integer, set it equal to -1 so executes the else portion of the conditional
    try:
      choice = int(choice)
    except ValueError:
      choice = -1 

    if choice == 1:
      easy_game(easy_list)
      break
    elif choice == 2:
      print("You have chosen Hard")
      # hard_game(hard_list)
      break
    else: 
      print("Invalid Option, try again\n")
      

def main():
  game_start()

if __name__ == "__main__":
    main()
