from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,postition):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(x=postition,y=0)

    def r_up(self):
        y_position = self.ycor()
        if y_position < 240:
            self.setposition(x=350,y=y_position + 20)

    def r_down(self):
        y_position = self.ycor()
        if y_position > -240:
            self.setposition(x=350,y=y_position - 20)

    def l_up(self):
        y_position = self.ycor()
        if y_position < 240:
            self.setposition(x=-350,y=y_position + 20)

    def l_down(self):
        y_position = self.ycor()
        if y_position > -240:
            self.setposition(x=-350,y=y_position - 20)