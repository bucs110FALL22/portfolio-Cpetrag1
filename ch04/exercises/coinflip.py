import turtle
import time
import random
turtle.getscreen()
t = turtle.Turtle()
t.shape("arrow")
gameon = True
while gameon:
  num = random.randrange(0,2)
  if num == 0:
    print("Heads!")
    t.left(90)
    t.fd(50)
  else:
    print("tails")
    t.right(90)
    t.fd(50)
  x = t.position()[0]
  y = t.position()[1]
  if x > 400 or x < -400:
    gameon = False
  elif y > 400 or y < -400:
    gameon = False
  else:
    gameon = True
print("loop is over x or y exceeded 400 or -400 which is off screen")
time.sleep(5)
    
    
    
    
    
  
  
  