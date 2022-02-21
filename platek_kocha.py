# rozwiązanie https://python-with-science.readthedocs.io/en/latest/koch_fractal/koch_fractal.html

from turtle import *


def koch(a, order):
    if order > 0:
        for t in [60, -120, 60, 0]:
            koch(a / 3, order - 1)
            left(t)
    else:
        forward(a)


color("sky blue", "white")
bgcolor("black")
size = 400
order = 7

penup()
backward(size/1.732)
left(30)
pendown()

tracer(100)
hideturtle()

begin_fill()

for i in range(3):
    koch(size, order)
    right(120)

end_fill()

update()
