def star_pyramid():
  x = int(input("Enter how many rows of stars: "))
  
  for i in range(x+1):
    print("*"*i)

star_pyramid()
def rstar_pyramid():
  x = int(input("Enter how many rows of stars: "))
  i = x
  while i >= 0:
    print("*"*i)
    i = i - 1

rstar_pyramid()