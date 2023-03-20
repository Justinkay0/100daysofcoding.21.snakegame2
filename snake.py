from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_list = []
        for _ in range(3):
            s = Turtle(shape='square')
            s.penup()
            s.color('white')
            s.setposition(y=0, x=0 - _ * 20)
            self.snake_list.append(s)
        self.head = self.snake_list[0]

    def move(self):
        for segments in range(len(self.snake_list) - 1, 0, -1):
            position = self.snake_list[segments - 1].pos()
            self.snake_list[segments].goto(x=position[0], y=position[1])
        self.snake_list[0].forward(20)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)