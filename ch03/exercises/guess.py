import random
num = random.randint(0,10)
guess = False
while guess == False:
  a = int(input("Guess a number 1-10: "))
  if a > num:
    print("Too high")
  if a < num:
    print("Too low")
  if a == num:
    print("correct")
    guess = True;
print("all done")
    
  
  
    
  
 