import turtle
window = turtle.Screen()
myturtle = turtle.Turtle()
myturtle.shape('arrow')
colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red']
#returns a str of colors
def colors_of_rainbow():
  str = ''
  for i in colors:
    str = str + " " + i
  return str
#Draws a rainbow and prints the colors within the rainbow (Calls the colors of rainbow fn)
def draw_rainbow(radius,startx,starty):
  myturtle.width(10)
  myturtle.left(90)
  print("These are the colors of a rainbow:" + colors_of_rainbow() + "!!")
  for i in colors:
    myturtle.penup()
    myturtle.goto(startx,starty)
    myturtle.pendown()
    myturtle.color(i)
    myturtle.circle(radius, 180)
    myturtle.left(180)
    starty = starty + 10
#first parameter is the radious of the circle and the second parameter is the starting x pos third parameter is y pos

#Calling the function
draw_rainbow(40,50,-50)

window.exitonclick()