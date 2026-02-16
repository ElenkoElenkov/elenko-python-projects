from turtle import *
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

# PLAYER
player = Turtle()
player.shape("triangle")
player.color("white")
player.penup()
player.goto(0, -250)
player.setheading(90)

# BULLET
bullet = Turtle()
bullet.shape("square")
bullet.color("yellow")
bullet.shapesize(stretch_wid=0.2, stretch_len=0.8)
bullet.penup()
bullet.hideturtle()
bullet.speed(0)

bullet_state = "ready"

# ENEMIES
enemies = []

for _ in range(5):
    enemy = Turtle()
    enemy.shape("circle")
    enemy.color("red")
    enemy.penup()
    enemy.goto(random.randint(-250, 250), random.randint(100, 250))
    enemies.append(enemy)

# SCORE
score = 0
scoreboard = Turtle()
scoreboard.hideturtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.goto(-260, 260)
scoreboard.write(f"Score: {score}", font=("Arial", 14, "normal"))


def move_left():
    x = player.xcor() - 20
    if x > -280:
        player.setx(x)


def move_right():
    x = player.xcor() + 20
    if x < 280:
        player.setx(x)


def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet.setposition(player.xcor(), player.ycor())
        bullet.showturtle()
        bullet_state = "fire"


def is_collision(t1, t2):
    return t1.distance(t2) < 20


listen()
onkey(move_left, "Left")
onkey(move_right, "Right")
onkey(fire_bullet, "space")

# GAME LOOP
game_on = True

while game_on:
    time.sleep(0.02)
    screen.update()

    # MOVE BULLET
    if bullet_state == "fire":
        bullet.sety(bullet.ycor() + 20)

    if bullet.ycor() > 280:
        bullet.hideturtle()
        bullet_state = "ready"

    # MOVE ENEMIES
    for enemy in enemies:
        enemy.sety(enemy.ycor() - 0.3)

        # COLLISION WITH BULLET
        if is_collision(bullet, enemy):
            bullet.hideturtle()
            bullet_state = "ready"
            enemy.goto(random.randint(-250, 250), random.randint(150, 250))
            score += 1
            scoreboard.clear()
            scoreboard.write(f"Score: {score}", font=("Arial", 14, "normal"))

        # GAME OVER
        if is_collision(player, enemy):
            game_on = False
            scoreboard.goto(0, 0)
            scoreboard.write("GAME OVER", align="center", font=("Arial", 20, "bold"))

screen.mainloop()