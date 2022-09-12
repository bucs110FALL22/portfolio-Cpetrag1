import turtle
my_screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
my_turtle.color("red")
sides = int(input("Enter the number of sides to your shape: "))
side_length = int(input("Enter the side length: "))
for i in range(sides):
 my_turtle.fd(side_length)
 my_turtle.left(360/sides)
my_screen.exitonclick()
