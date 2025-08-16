from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_pos = 10
        self.y_pos = 10
        self.move_speed = 0.1

    def move(self):
        x_pos = self.xcor() + self.x_pos
        y_pos = self.ycor() + self.y_pos
        self.goto(x_pos,y_pos)

    def bounce_y(self):
        self.y_pos *= -1

    def bounce_x(self):
        self.x_pos *= -1
        self.move_speed *= 0.95

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed =0.1
