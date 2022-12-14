from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # self.shape("dot")
        self.color("white")
        self.shape("circle")
        self.penup()
        self.xmove = 10
        self.ymove = -10

    def move(self):
        x_cor = self.xcor() + self.xmove
        y_cor = self.ycor() + self.ymove
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1.02


    def reset(self):
        self.goto(0, 0)
        self.bounce_x()