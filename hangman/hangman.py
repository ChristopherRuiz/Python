import random

# Global Variable Declaration
game_over = 6
easy_list = ["drive","seat","stop","sled","lie"]
hard_list = ["unknown","yummy","espionage","hyphen","rhythm"]
graphic = ['''
    +---+
        |
        |
        |
      ===''', '''
    +---+
    O   |
        |
        |
      ===''', '''
    +---+
    O   |
    |   |
        |
      ===''', '''
    +---+
    O   |
   /|   |
        |
      ===''', '''
    +---+
    O   |
   /|\  |
        |
      ===''', '''
    +---+
    O   |
   /|\  |
   /    |
      ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
      ===''']

# Draw the character in a 2d Array given different guessesA
def draw_current(guesses):
  if guesses == 0:
    print(graphic[0])
  elif guesses == 1:
    print(graphic[1])
  elif guesses == 2:
    print(graphic[2])
  elif guesses == 3:
    print(graphic[3])
  elif guesses == 4:
    print(graphic[4])
  elif guesses == 5:
    print(graphic[5])
  elif guesses == 6:
    print(graphic[6])


# Game of Hangman
def game(game_list):
  # Some variable declarations for the game
  guess_count = 0
  game_word = game_list[random.randint(0,4)]
  word_count = len(game_word)
  word_char = list(game_word)
  guess_list = []

  draw_current(guess_count)                               # draw the game graphic
  for i in range(word_count):                             # Printing out blank spaces for the letters in the word
    guess_list.append("_")
    print("_", end=' ')
  print("\n")

  # While loop to iterate  until all guesses have been used(game over) or the user guesses the word correctly 
  while guess_count != game_over | word_count >= 0:
    guess = input("Enter your guess: ")                   # draw_current(guess_count) 

    # If letter guessed is in the word list(word_char), then insert the value in the guess_list at the index the letter was found in the word list
    if guess.lower() in word_char:
      print("Correct!", guess.lower(), "is in the word")
      guess_list[word_char.index(guess)] = guess      
      draw_current(guess_count)

      for i in guess_list:                                # print out the updated game board
        print(i, end=' ')
      print("\n")
      
      word_count -= 1
      if word_count == 0:                                 # Exit game when won
        print("You won!")
        break
    
    elif guess.lower() not in word_char:
      guess_count += 1
      print(guess.lower(),"is not in the word")
      draw_current(guess_count)

      for i in guess_list:                                # print current guessed letters in word 
        print(i, end=' ')
      print("\n")

      if guess_count == 6:                                # Exit game when lost
        print("You Lost...")
        draw_current(guess_count)
        break

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
      game(easy_list)
      break
    elif choice == 2:
      game(hard_list)
      break
    else: 
      print("Invalid Option, try again\n")
      

def main():
  game_start()

if __name__ == "__main__":
    main()
