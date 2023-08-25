from turtle import Turtle

SPEED = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.angle = 45
        self.shape("circle")
        self.color("white")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.setheading(self.angle)

    def bounce_x(self):
        self.angle *= 3
        self.setheading(self.angle)

    def bounce_y(self):
        self.angle *= -1
        self.setheading(self.angle)

    def update_position(self):
        if abs(self.ycor()) > 285:
            self.bounce_y()

        self.forward(SPEED)
