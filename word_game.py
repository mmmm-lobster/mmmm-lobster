word = "chair" #set the word here, scroll down, hit play,
#and let someone else try to guess it!
#I didnt know how to make it check if the word guessed is a real word,
#so it's on the honor system lol.






































print("You have 5 tries to guess the 5 letter word.")
print(" Every guess tells you how many letters your guess  shares with the word")
def checkguess(guess):
  validguess = True
  correctnums = 0
  GameWon = False
  if len(guess) ==5:
    
    correctnums = 0
    for x in guess:
     if x in word:
       correctnums = correctnums + 1
   
    if guess == word:
      GameWon = True
    
  else:
    validguess = False
  return(validguess,correctnums,GameWon)

for i in range(1,21):
 
  guess = input("Guess a 5 letter word: ")
  guesschecked = checkguess(guess)
  if not guesschecked[2]:
    if guesschecked[0]:
      print(f"Your word shares {guesschecked[1]} letter(s) with the word")
      print(f"You have used {i} of your 20 guesses")
    else:
      print("Word must be 5 letters long")
  else:
    print("You won! :D")
    break
  if i == 20:
    print(f"You lost. The word was '{word}' ):")
    

# print("Game Ended")
