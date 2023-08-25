from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
ball = Ball()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Пенг Понг")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    ball.update_position()
    screen.update()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 335 or ball.distance(l_paddle) < 50 and ball.xcor() < -335:
        ball.bounce_x()

screen.exitonclick()
