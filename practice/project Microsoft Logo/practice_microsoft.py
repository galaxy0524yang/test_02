# マイクロソフト ロゴ 練習

import turtle

#左上
turtle.penup()
turtle.goto(-180,180)
turtle.pendown()

a = 0
while a < 4:
    turtle.forward(165)
    turtle.right(90)
    a += 1

#右上
turtle.penup()
turtle.goto(15,180)
turtle.pendown()

a = 0
while a < 4:
    turtle.forward(165)
    turtle.right(90)
    a += 1

#左下
turtle.penup()
turtle.goto(-180,-15)
turtle.pendown()

a = 0
while a < 4:
    turtle.forward(165)
    turtle.right(90)
    a += 1

#右下
turtle.penup()
turtle.goto(15,-15)
turtle.pendown()

a = 0
while a < 4:
    turtle.forward(165)
    turtle.right(90)
    a += 1

# #外枠
# turtle.penup()
# turtle.goto(265,0)
# turtle.pendown()
# turtle.left(90)
# turtle.circle(265)

turtle.hideturtle()
turtle.done()




'''
# 右下
a = 0
while a < 4:
    turtle.forward(50)
    turtle.right(90)
    a += 1

# 右上
turtle.penup()
turtle.goto(0,60)
turtle.pendown()

a = 0
while a < 4:
    turtle.forward(50)
    turtle.right(90)
    a += 1

# 左下
turtle.penup()
turtle.goto(-60,0)
turtle.pendown()

a = 0
while a < 4:
    turtle.forward(50)
    turtle.right(90)
    a += 1

# 左上
turtle.penup()
turtle.goto(-60,60)
turtle.pendown()

a = 0
while a < 4:
    turtle.forward(50)
    turtle.right(90)
    a += 1

turtle.hideturtle()

turtle.done()
'''