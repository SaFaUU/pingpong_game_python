from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from  scoreboad import  Scoreboad
import time

screen = Screen()
ball = Ball()
screen.tracer(0)
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
score= Scoreboad()
game_is_on = True
screen.listen()
screen.onkeypress(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=r_paddle.go_down, key="Down")
screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=l_paddle.go_down, key="s")
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.1)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset()
        score.l_point()
    elif ball.xcor() < -380:
        ball.reset()
        score.r_point()
screen.exitonclick()
