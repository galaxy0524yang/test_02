# マイクロソフト ロゴ 練習

from turtle import *
setup(1000, 1000, 0, 0)

White = "#FFFFFF"
OrangeRed = '#F25022'
Green = '#7FBA00'
Blue = '#00A4EF'
Yellow = '#FFB900'

# 正方形を描く関数を定義
def Square(x, y, color1, color2):
    penup()
    goto(x, y)      # スタート位置座標入力
    pendown()

    color(color1, color2)       # color1 は枠線色、color2 は中身色
    begin_fill()
    for a in range(4):
        forward(175)
        right(90)
    end_fill()

# #左上
Square(x = -180, y = 180, color1 = White, color2 = OrangeRed)

# #右上
Square(x = 15, y = 180, color1 = White, color2 = Green)

# #左下
Square(x = -180, y = -15, color1 = White, color2 = Blue)

# #右下
Square(x = 15, y = -15, color1 = White, color2 = Yellow)


hideturtle()
done()