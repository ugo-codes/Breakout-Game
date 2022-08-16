import random
from turtle import Turtle


class Ball(Turtle):
    """
    This class is the ball that shows uo on the screen
    """

    def __init__(self):
        # initializes the Turtle class
        Turtle.__init__(self)
        # change the color of the ball to white
        self.color("white")
        # change the shape of the ball to circle
        self.shape("circle")
        # raises the pen of the turtle up to avoid draing lines
        self.penup()
        # moves the ball to the starting position
        self.goto(x=0, y=-260)
        # create a list of coordinates
        self.cors = [1, -1]
        # randomly pick the starting x coordinates direction, either left or right side
        self.x_cor = 10 * random.choice(self.cors)
        # sets the y coordinates in the positive y direction
        self.y_cor = 10

    def move(self):
        """
        This method moves the ball 10 pixels forward
        :return: None
        """
        # create a new x and y coordinates from the current ball coordinates
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        # move the ball 10 pixels forward
        self.goto(x=new_x, y=new_y)

    def bounce(self):
        """
        This method bounces the ball by changing the direction of the y coordinates and randomly picking the direction
         of the x coordinates
        :return: None
        """
        self.y_cor *= -1
        self.x_cor *= random.choice(self.cors)

    def bounce_x(self):
        """
        This method bounces the ball in the x direction by changing the direction of the x coordinates
        :return: None
        """
        self.x_cor *= -1

    def bounce_y(self):
        """
        This method bounces the ball in the y direction by changing the direction of the ball in the y coordinates
        :return: None
        """
        self.y_cor *= -1
