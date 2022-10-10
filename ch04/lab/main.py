import pygame
import random
import math
import time
pygame.init()
surface = pygame.display.set_mode((400,400))
def dartboard():
  pygame.draw.rect(surface, "blue", pygame.Rect(0,0,400,400))
  pygame.draw.circle(surface, "red", (200,200), 200)
  pygame.draw.line(surface, "black", (200,0), (200,400))
  pygame.draw.line(surface, "black", (0,200), (400,200))
dartboard()
pygame.display.flip()
for i in range(11):
  x = random.randrange(0,401)
  y = random.randrange(0,401)
  distance_from_center = math.hypot(200-x, 200-y) #the distance formula
  is_in_circle = distance_from_center <= 400/2 #screen width
  if is_in_circle:
      pygame.draw.circle(surface, "green", (x,y), 3)
  else:
      pygame.draw.circle(surface, "white", (x,y), 3)
pygame.display.flip()
time.sleep(3)
dartboard()
pygame.draw.rect(surface, "blue", pygame.Rect(50,200,100,100))
pygame.draw.rect(surface, "red4", pygame.Rect(250,200,100,100))
pygame.display.flip()
time.sleep(3)
dartboard()
pygame.display.flip()
time.sleep(3)
print("Press on blue if you think player1 wins and red if you think player2 wins!")

# for event in pygame.event.get():
#   if event.pos[0] > 50 & event.pos[0] < 150 & event.pos[1] > 200 & event.pos[1] < 300:
#     print("You chose player1 to win")
#   if event.pos[0] > 250 & event.pos[0] < 350 & event.pos[1] > 200 & event.pos[1] < 300:
#     print("You chose player2 to win")
# for event in pygame.event.get():
#   if event.type == pygame.MOUSEBUTTONDOWN:
#     x = event.pos[0]
#     y = event.pos[1]
#   if x > 50 & x < 150 & y > 200 & y < 300:
#     print("you chose player1")
#   if x > 250 & x < 350 & y > 200 & y < 300:
#     print("you chose player2") 




#***I Dont know how to use mouse for input so that part is not answered***


score1 = 0
score2 = 0
print("player1 is green darts")
print("player2 is black darts")
for i in range(11):
  print("plyaer 1 throws")
  x = random.randrange(0,401)
  y = random.randrange(0,401)
  distance_from_center = math.hypot(200-x, 200-y) #the distance formula
  is_in_circle = distance_from_center <= 400/2 #screen width
  if is_in_circle:
    pygame.draw.circle(surface, "green", (x,y), 3)
    pygame.display.flip()
    print("hit")
    score1 = score1 + 1
  else:
    pygame.draw.circle(surface, "white", (x,y), 3)
    pygame.display.flip()
    print("miss")
  print("player2 throws")
  x = random.randrange(0,401)
  y = random.randrange(0,401)
  distance_from_center = math.hypot(200-x, 200-y) #the distance formula
  is_in_circle = distance_from_center <= 400/2 #screen width
  if is_in_circle:
    pygame.draw.circle(surface, "black", (x,y), 3)
    pygame.display.flip()
    print("hit")
    score2 = score2 + 1
  else:
    pygame.draw.circle(surface, "white", (x,y), 3)
    pygame.display.flip()
    print("miss")
if score1 > score2:
  print("player1 wins")
elif score2 > score1:
  print("player2 wins")
else:
  print("TIE!")
time.sleep(5)