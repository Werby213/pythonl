import turtle
color = ["blue", "yellow", "black", "green", "red"]
t = turtle.Turtle()
a=0
x=0
y=0
t.speed(1000)
t.width(20)
for i in range(5):
    t.color(color[i])
    t.up()
    t.goto(x, y)
    t.down()
    y+=100
    t.circle(120)
    y += 100
    x+=110
    if y >=200:
        y-=400
turtle.done()