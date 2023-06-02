import random
import turtle
import time

megafoodcolor = ["white","gold"]
color = ["white", "red", "blue", "yellow", "green"]
shape = ["turtle", "circle", "square",]

snake, window, food, trap, megafood, count, borders = turtle.Turtle(), turtle.Screen(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()

count.up()
count.color("white")
count.hideturtle()
count.goto(-70,250)
high_score = 1

def border():
    borders.color("red")
    borders.width(5)
    borders.penup()
    borders.goto(-300,-300)
    borders.pendown()
    for i in range (4):
        borders.forward(600)
        borders.left(90)

trap.up()
food.up()
food.shape("circle")
food.color("white")
food.goto(0,100)
direction="stop"
snake.up()
score = 0
high_score = 0
snake.shape("square")
snake.color("red")
tail = []

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
window.setup(1200,620)
window.listen()
border()

window.onkeypress(snake_up, "w")
window.onkeypress(snake_left, "a")
window.onkeypress(snake_down, "s")
window.onkeypress(snake_right, "d")

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

        for segment in tail:
            segment_turtle = turtle.Turtle()
            segment_turtle.shape("square")
            segment_turtle.color("red")
            segment_turtle.goto(segment)
while True:
    move()
    window.update()
    time.sleep(0.1)
    tail.insert(0, snake.position())
    if len(tail) > score:
        tail.pop()

    if snake.distance(megafood) < 20:
        for i in range (random.randint(3,10)):
            megafood.goto(random.randint(-280, 280), random.randint(-280, 280))
            megafood.shape(random.choice(shape))
            megafood.color(random.choice(megafoodcolor))
        score += 3
        print(score)
        count.clear()
        score1(score)
    if snake.distance(food) < 20:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        score += 1
        tail.append(2)
        print(score)
        count.clear()
        score1(score)
        food.shape(random.choice(shape))
        food.color(random.choice(color))
    for segment in tail:
        if snake.distance(segment) < 20:
            print("Game Over")
            time.sleep(2)
            snake.goto(0, 0)
            snake.direction = "stop"
            tail.clear()
            score = 0
            count.clear()
            score1(score)
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        print("Game Over")
        time.sleep(2)
        snake.goto(0, 0)
        snake.direction = "stop"
        tail.clear()
        score = 0
        count.clear()
        score1(score)
