import turtle
t = turtle.Turtle()
a=0
x=0
y=0
t.speed(0)
for i in range(74):
    x = x + 100
    a = a + 45
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.goto(x, 0)
    if a >= 45:
        t.left(a)
        a = a - 45
    else:
        t.left(a)
turtle.done()