from turtle import Turtle


class Paddle(Turtle):
    """
    This class represents the paddles used in the game
    """

    def __init__(self):
        # initializes the turtle class
        Turtle.__init__(self, shape="square")
        # changes the color of the brick to white
        self.color("white")
        # stretches the length of the brick by 7
        self.shapesize(stretch_len=7)
        # raises the pen of the turtle to avoid drawing on the screen
        self.penup()
        # moves the paddle to the starting position
        self.goto(0, -280)

    def go_left(self):
        """
        This method moves the paddle move left
        :return: None
        """
        # get the current x coordinates and subtract 20 from it
        new_x_cor = self.xcor() - 20
        # move to the new coordinates gotten
        self.goto(x=new_x_cor, y=self.ycor())

    def go_right(self):
        """
        This method moves the paddle right
        :return: None
        """
        # get the current x coordinates and add 20 from it
        new_x_cor = self.xcor() + 20
        # move to the new coordinates gotten
        self.goto(x=new_x_cor, y=self.ycor())
