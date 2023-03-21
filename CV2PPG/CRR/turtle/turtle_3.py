import turtle
coord = [[0,0],[-80,-200],[100,-80],[-100,-80],[80,-200],[0,0]]
t = turtle.Turtle()
t.speed(1000)
for i in range(len(coord)):
        t.up()
        t.goto(coord[i][0],coord[i][1])
        t.down()
        t.filling()
        t.dot(10, "red")
turtle.done()