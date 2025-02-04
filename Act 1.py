import turtle
turtle.Screen().bgcolor("white")
turtle.Screen().setup(500,500)
poly=turtle.Turtle
side=6
lenn=100
angle=360/side

for i in range(side):
    turtle.forward(lenn)
    turtle.right(angle)

turtle.done()