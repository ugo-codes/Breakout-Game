from turtle import Turtle


class Bricks(Turtle):
    """
    This clas represents the brick used in the game
    """

    def __init__(self):
        # initializes the turtle class
        Turtle.__init__(self)
        # changes the color of the brick to green
        self.color("green")
        # change the shape of the brick to square
        self.shape("square")
        # stretches the length of the brick by 2
        self.shapesize(stretch_len=2)
        # raises the pen of the turtle to avoid drawing on the screen
        self.penup()
