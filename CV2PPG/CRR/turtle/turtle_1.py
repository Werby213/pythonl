import turtle
t = turtle.Turtle()
a=60
t.speed(100000)
for i in range(30):
    t.forward(100)
    t.right(a)
    a += 60
    t.forward(100)
turtle.done()