import random
import turtle
import time
megafoodcolor = ["white","gold"]
color = ["white", "red", "blue", "yellow", "green"]
shape = ["turtle", "circle", "square",]
segments = []
snake, count, borders = [turtle.Turtle() for _ in range(3)]
foods = [turtle.Turtle() for _ in range(5)]
for food in foods:
    food.up()
megafoods = [turtle.Turtle() for _ in range(2)]
for megafood in megafoods:
    megafood.up()
traps = [turtle.Turtle() for _ in range(10)]
for trap in traps:
    trap.up()
for food in foods:
    food.up()
window = turtle.Screen()
count.up()
turtle.color("red")
count.color("white")
count.hideturtle()
count.goto(-70,250)
high_score = 1
speed = 0.2
def border():
    borders.color("red")
    borders.width(5)
    borders.penup()
    borders.goto(-300,-300)
    borders.pendown()
    for i in range (4):
        borders.forward(600)
        borders.left(90)
food.shape("circle")
food.color("white")
food.goto(0,100)
direction = "stop"
snake.up()
score = 0
high_score = 0
snake.shape("square")
snake.color("red")
def snake_up():
    global direction
    if direction != "down":
        direction = "up"
    pass
def snake_down():
    global direction
    if direction != "up":
        direction = "down"
    pass
def snake_right():
    global direction
    if direction != "left":
        direction = "right"
    pass
def snake_left():
    global direction
    if direction != "right":
        direction = "left"
    pass
direction = 100
window.title("Snake Game 2 windows 10 super redux ultra definition edition by XXXnagibatorEgorsuperprogamer3000_228_1488XXX")
window.bgcolor("black")
window.tracer(0)
window.setup(620,620)
window.listen()
border()
window.onkeypress(snake_up, "w")
window.onkeypress(snake_left, "a")
window.onkeypress(snake_down, "s")
window.onkeypress(snake_right, "d")
def pause():
    window.onkeypress(pause, "p")
def move():
    if direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)
    if direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
def score1(score):
    count.write("Score: {} High Score: {} ".format(score, high_score), align="center", font=("Crixus", 24, "bold"))
while True:
    for i in range(len(segments) - 1, 0, -1):
            x = segments[i - 1].xcor()
            y = segments[i - 1].ycor()
            segments[i].goto(x, y)
    if len(segments) > 0:
        segments[0].goto(snake.xcor(), snake.ycor())
#food
    move()
    for segment in segments:
        if segment.distance(snake) < 20:
            snake.goto(0, 0)
            snake.direction = "Stop"
            for segment in segments:
                snake.goto(1000,1000)
                segment.goto(1000, 1000)
            segments.clear()
    for food in foods:
        if snake.distance(food) < 20:
            segment = turtle.Turtle()
            segment.color("red")
            segment.shape("square")
            segment.penup()
            segment.speed(0)
            segments.append(segment)
            food.goto(random.randint(-280, 280), random.randint(-280, 280))
            food.color(random.choice(color))
            food.shape(random.choice(shape))
            score += 1
            if speed > 0.10:
                speed -= 0.02
            count.clear()
            score1(score)
    for megafood in megafoods:
        if snake.distance(megafood) < 20:
            megafood.goto(random.randint(-280, 280), random.randint(-280, 280))
            food.shape(random.choice(shape))
            score += 2
            count.clear()
            score1(score)
#trap
    for trap in traps:
        if snake.distance(trap) < 20:
            trap.goto(random.randint(-280, 280), random.randint(-280, 280))
            trap.color(random.choice(color))
            trap.shape("triangle")
            segments.clear()
            score = 0
            speed = 0.5
            count.clear()
            score1(score)
            for i in segments:
                snake.goto(1000, 1000)
                segment.goto(1000, 1000)
                i.hideturtle()
            segments.clear()
            snake.goto(0, 0)
            direction = "stop"
#border
    if score < 3:
        if snake.ycor() == 300 or snake.ycor() == -300 or snake.xcor() == 300 or snake.xcor() == -300:
            segments.clear()
            snake.goto(0,0)
            segments.clear()
            count.clear()
            print(score)
            score1(score)
            for i in segments:
                snake.goto(1000, 1000)
                segment.goto(1000, 1000)
                i.hideturtle()
            segments.clear()
            direction = "stop"
        if score >= high_score:
            count.clear()
            score1(score)
            high_score = score
    else:
        if snake.xcor() >= 290: #правая стенка
            snake.setx(-280)
            print("правая стенка")
        if snake.ycor() >= 290: #верхняя стенка
            snake.sety(-280)
            print("верхняя стенка")
        if snake.xcor() <= -290: #левая стенка
            snake.setx(280)
            print("левая стенка")
        if snake.ycor() <= -290: #нижняя стенка
            snake.sety(280)
            print("нижняя стенка")
            print(score)
            score1(score)
        if score >= high_score:
            count.clear()
            score1(score)
            high_score = score
    window.update()
    time.sleep(speed)