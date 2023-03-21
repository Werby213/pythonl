import turtle
t = turtle.Turtle()
a=0
t.speed(10000)
for i in range(74):
    for i in range(4):
        t.forward(200)
        t.left(90)
    t.home()
    t.left(a)
    a=a+5
turtle.done()