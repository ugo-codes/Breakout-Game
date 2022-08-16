import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks

# the x coordinates for placing the bricks
bricks_x_cor = -360
# the y coordinates for placing the bricks
bricks_y_cor = 290
# a lst of all the bricks created
bricks = []

# the screen for interface
screen = Screen()
# change the background color of the screen to black
screen.bgcolor("black")
# set the title of the screen
screen.title("Breakout")
# set the width and height of the screen
screen.setup(width=800, height=600)
# disable the screen from updating itself
screen.tracer(0)

# create a paddle on the screen
paddle = Paddle()
# create a ball on the screen
ball = Ball()

# loop through a number of bricks
for index in range(1, 61):
    # create a brick
    brick = Bricks()
    # places the brick at a particular position on the screen
    brick.goto(x=bricks_x_cor, y=bricks_y_cor)
    # change the brick x coordinates
    bricks_x_cor += 65

    # set the brick x and y coordinates after a particular number of times
    if index % 12 == 0:
        bricks_x_cor = -360
        bricks_y_cor -= 25

    # add the newly created brick to the list
    bricks.append(brick)

# add a listener to the screen to listen for event
screen.listen()
# listen to the arrow left key event
screen.onkey(paddle.go_left, "Left")
# listen to the arrow right key event
screen.onkey(paddle.go_right, "Right")

# creates a variable called game is on
game_is_on = True

while game_is_on:
    # make the loop pause for 0.1 seconds
    time.sleep(0.1)
    # update the screen
    screen.update()
    # move the ball for a particular distance
    ball.move()

    # Detect collision with the paddle
    if ball.distance(paddle) < 60 and ball.ycor() <= -260:
        ball.bounce()

    # Detect collision with the brick
    for brick in bricks:
        if ball.distance(brick) <= 20:
            brick.hideturtle()
            bricks.remove(brick)
            ball.bounce()

    # Detect collision with the bottom wall
    if ball.ycor() <= -300:
        # end game
        game_is_on = False

    # Detect collision with the top wall
    if ball.ycor() >= 300:
        ball.bounce_y()

    # Detect collision with the side of the walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

# the screen keeps itself visible and only exit once the exit key is pressed
screen.exitonclick()
