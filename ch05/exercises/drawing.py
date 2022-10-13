import turtle
s = turtle.Screen()
def DrawEqShape(t,num_sides,side_length):
  for i in range(num_sides):
    t.fd(side_length)
    t.left(360/num_sides)
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
num_sides = int(input("enter how many sides: "))
side_length = int(input("enter side length: "))
DrawEqShape(t, num_sides, side_length)
s.exitonclick()