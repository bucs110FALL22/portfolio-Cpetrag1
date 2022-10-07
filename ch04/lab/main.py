import pygame
import random

pygame.init()
surface = pygame.display.set_mode((500,500))
color = (0,0,255)
ccolor = (255,0,0)
pygame.draw.rect(surface, color, pygame.Rect(0,0,500,500))
pygame.draw.circle(surface, ccolor, (250,250), 500)
pygame.display.flip()
for i in range(11):
  x = random.randrange(0,501)
  y = random.randrange(0,501)
  distance_from_center = math.hypot(x1-x2, y1-y2) #the distance formula
  is_in_circle = distance_from_center <= width/2 #screen width
  if is_in_circle:
    c = (0,255,0)
  else:
    c = (150,0,0)
  pygame.draw.circle(surface, c, (x,y), 3)
  pygame.display.flip()

  