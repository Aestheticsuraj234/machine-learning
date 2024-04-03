import random

target = random.randint(1, 100)

while True:
  userChoice = int(input("Guess the target :"))
  if(userChoice == target):
      print("Success : Correct Guess!!!")
      break
  elif(userChoice < target):
      print("Your number was too Small. Take a bigger guess...")
  else:
      print("Your number was too big. take a smaller guess")    
      
      
    
print("Game over!")