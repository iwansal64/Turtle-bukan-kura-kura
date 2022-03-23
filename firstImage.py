import turtle
from random import choice

turtle.speed(6)

height = turtle.window_height()
width = turtle.window_width()

centerWidth = width // 2
centerHeight = height // 2

startPos = (centerWidth + 250, centerHeight + 250)

squareSize = 20
factorScale = 10
iteration = 10

color = []
defaultColor = [["#008288", "#00968e", "#106e7c", "#2a4858"], ["#39b48e", "#4ebf8b", "#64c987", "#7bd283"]]
colormode = "todark" # random, todark, tobright

direction1 = "up"
direction2 = "left"
directionStack = ["left", "down"]

mode = "stack"

# ===== Setup =====
turtle.penup()
turtle.bgcolor("#000000")
turtle.color("#FFFFFF")

gotoPosX = startPos[0] - centerWidth
gotoPosY = startPos[1] - centerHeight

if gotoPosX < 0:
    turtle.forward(+gotoPosX)
else:
    turtle.backward(+gotoPosX)

if gotoPosY < 0:
    turtle.left(90)
        
else:
    turtle.right(90)

turtle.backward(+gotoPosY)
if direction1 == "up":
    turtle.setheading(90)
elif direction1 == "down":
    turtle.setheading(270)

turtle.pendown()
colorReference = choice(defaultColor)
# ===== Draw =====
for index, i in enumerate(range(iteration, 1, -1)):
    try:
        turtle.fillcolor(color[i - 1])
    except:
        if colormode == "tobright":
            try:
                turtle.fillcolor(colorReference[len(colorReference) - index + 1])
            except:
                turtle.fillcolor(colorReference[0])
        elif colormode == "todark":
            try:
                turtle.fillcolor(colorReference[index])
            except:
                turtle.fillcolor(colorReference[len(colorReference) - 1])

        elif colormode == "random":
            turtle.fillcolor(choice(colorReference))
        else:
            turtle.fillcolor("white")

    turtle.penup()
    
    currentsize = squareSize + factorScale * (i + 1)
    if mode == "center":
        turtle.goto((currentsize // 2 - i - gotoPosX, currentsize // 2 - i - gotoPosY))

    turtle.pendown()

    turtle.begin_fill()
    
    if (direction2 == "left" and direction1 == "up") or (direction2 == "right" and direction1 == "down"):
        turtle.forward(currentsize)
        turtle.left(90)
        turtle.forward(currentsize)
        turtle.left(90)
        turtle.forward(currentsize)
        turtle.left(90)
        turtle.forward(currentsize)
        turtle.left(90)
    else:
        turtle.forward(currentsize)
        turtle.right(90)
        turtle.forward(currentsize)
        turtle.right(90)
        turtle.forward(currentsize)
        turtle.right(90)
        turtle.forward(currentsize)
        turtle.right(90)
    
    turtle.end_fill()

    turtle.penup()

    if mode == "stack":
        if directionStack[0] == "left":
            if directionStack[1] == "up":
                turtle.goto((-20 * (index + 1), (20 * (index + 1))))
            elif directionStack[1] == "down":
                turtle.goto((-20 * (index + 1), (-20 * (index + 1))))
        elif directionStack[0] == "right":
            if directionStack[1] == "up":
                turtle.goto((20 * (index + 1), (20 * (index + 1))))
            elif directionStack[1] == "down":
                turtle.goto((20 * (index + 1), (-20 * (index + 1))))

    
    elif mode == "center":
        turtle.goto((currentsize // 2 - i - gotoPosX, currentsize // 2 - i - gotoPosY))
    
    turtle.pendown()

turtle.done()