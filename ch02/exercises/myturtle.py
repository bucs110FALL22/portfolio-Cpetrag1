import turtle
my_screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
my_turtle.color('purple')
for i in [1,2,3,4]:
  my_turtle.fd(50)
  my_turtle.left(90)

my_turtle.color('red')
my_turtle.penup()
my_turtle.setpos(-75,0)
my_turtle.pendown()
for i in [1,2,3,4]:
  my_turtle.fd(50)
  my_turtle.left(90)
my_screen.exitonclick()