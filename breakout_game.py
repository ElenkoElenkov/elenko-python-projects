from turtle import *
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# PADDLE
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

def move_left():
    paddle.setx(paddle.xcor() - 40)

def move_right():
    paddle.setx(paddle.xcor() + 40)

screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# BALL
ball = Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx = 3
ball.dy = 3

# BRICKS
bricks = []

for x in range(-350, 350, 100):
    for y in range(200, 260, 30):
        brick = Turtle()
        brick.shape("square")
        brick.color("red")
        brick.shapesize(stretch_wid=1, stretch_len=4)
        brick.penup()
        brick.goto(x, y)
        bricks.append(brick)

# GAME LOOP
game_on = True

while game_on:
    time.sleep(0.01)
    screen.update()

    ball.goto(ball.xcor() + ball.dx, ball.ycor() + ball.dy)

    # WALL BOUNCE
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.dx *= -1

    if ball.ycor() > 280:
        ball.dy *= -1

    # PADDLE BOUNCE
    if ball.distance(paddle) < 50 and ball.ycor() < -230:
        ball.dy *= -1

    # BRICK COLLISION
    for brick in bricks:
        if ball.distance(brick) < 50:
            ball.dy *= -1
            brick.hideturtle()
            bricks.remove(brick)

    # GAME OVER
    if ball.ycor() < -290:
        game_on = False

screen.mainloop()