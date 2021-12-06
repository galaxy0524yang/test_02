import turtle

t = turtle.Pen()
t.speed("fastest")
t.color("red")
t.width(5)

for x in range(400):
    # t.speed("fastest")
    t.forward(x)
    t.left(60)

t.hideturtle()
turtle.done()
