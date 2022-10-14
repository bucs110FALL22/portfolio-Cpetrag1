import pygame
import time
# Part A
n = 101
loop = True
while loop:
  if n % 2 == 0:
    n = n/2
    print(n)
  else:
    n = 3*n + 1
    print(n)
  if n == 1:
    loop = False
# Part B 
n = 101
count = 0
loop = True
while loop:
  if n % 2 == 0:
    n = n/2
    print(n)
  else:
    n = 3*n + 1
    print(n)
  if n == 1:
    loop = False
  count = count + 1
print("The number of interations is: " + str(count))
upper_limit = 20
iters = {}
for start in range(2, upper_limit+1):
  n = start
  count = 0
  loop = True
  while loop:
    if n % 2 == 0:
      n = n/2
      print(n)
    else:
      n = 3*n + 1
      print(n)
    if n == 1:
      loop = False
    count = count + 1
  iters[start] = count
print(iters)
#part C
pygame.init()
display = pygame.display.set_mode((500,500))
font = pygame.font.Font(None, 12)
upper_limit = 20
iters = {}
max_so_far = 0
max_val = 0
scale = 5
for i in range(2, upper_limit):
  new_display = pygame.transform.flip(display, False, True)
  display.blit( new_display , (0, 0) )
  count = 0
  n = i
  loop = True
  while loop:
    if n % 2 == 0:
      n = n/2
    else:
      n = 3*n + 1
    if n == 1:
      loop = False
    count = count + 1
  iters[i] = count
  x = iters.items()
  items = tuple(x)
  if len(items) >= 2:
    pygame.draw.lines(display, "black", False, items)
  pygame.display.flip()
  if max_so_far < count:
    max_so_far = count
  print(max_so_far)
  max_val = max_so_far
  msg = "The curret maximum number of iterations is: " + str(max_so_far)
  msg = font.render(msg , False, "red")
  display.blit(msg, (10,10))
  pygame.display.flip()
time.sleep(5)
