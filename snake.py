from turtle import Turtle, Screen
screen = Screen()

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in range(3):
            snakey = Turtle("square")
            snakey.color("dark green")
            snakey.penup()
            snakey.goto(position, 0)
            self.body.append(snakey)

    def move(self):

        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_segment(self, position):
        snakey = Turtle("square")
        snakey.color("green")
        snakey.penup()
        snakey.goto(position)
        self.body.append(snakey)

    def extend(self):
        self.add_segment(self.body[-1].position())

    def reset(self):
        for segments in self.body:
            segments.goto(1000, 1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

