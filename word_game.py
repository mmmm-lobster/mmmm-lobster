word = "chair" #set the word here, scroll down, hit play,
#and let someone else try to guess it!
#I didnt know how to make it check if the word guessed is a real word,
#so it's on the honor system lol.





































game_ended = False
print("You have 5 tries to guess the 5 letter word.")
print(" Every guess tells you how many letters your guess  shares with the word")
def checkguess(guess):
  if len(guess) ==5:
    correctnums = 0
    for x in guess:
     if x in word:
       correctnums = correctnums + 1
    print(correctnums)
    if guess == word:
      print("You did it!!!")
      global game_ended
      game_ended = True
  else:
    print("Guess needs to be 5 letters")
for _ in range(1,20):
  if not game_ended:
    guess = input("Guess a 5 letter word: ")
    checkguess(guess)

print("Game Ended")