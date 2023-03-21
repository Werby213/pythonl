def drawFilledSquare(size, depth):
    size = int(size)

    # Move to the top-right corner before drawing:
    turtle.penup()
    turtle.forward(size // 2)
    turtle.left(90)
    turtle.forward(size // 2)
    turtle.left(180)
    turtle.pendown()

    # Alternate between white and gray (with black border):
    if depth % 2 == 0:
        turtle.pencolor('black')
        turtle.fillcolor('white')
    else:
        turtle.pencolor('black')
        turtle.fillcolor('gray')

    # Draw a square:
    turtle.begin_fill()
    for i in range(4):  # Draw four lines.
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()


def drawTriangleOutline(size, depth):
    size = int(size)

    # Move the turtle to the top of the equilateral triangle:
    height = size * math.sqrt(3) / 2
    turtle.penup()
    turtle.left(90)  # Turn to face upwards.
    turtle.forward(height * (2/3))  # Move to the top corner.
    turtle.right(150)  # Turn to face the bottom-right corner.
    turtle.pendown()

    # Draw the three sides of the triangle:
    for i in range(3):
        turtle.forward(size)
        turtle.right(120)