import turtle as t


class Snake:

    def __init__(self, s):
        self.seg_no = s
        self.segments = []
        self.snake_maker()

    def snake_maker(self):
        for i in range(0, self.seg_no):
            segment = t.Turtle()
            coord = (-20*i, 0)
            segment.up()
            segment.goto(coord)
            segment.shape("square")
            segment.color("white")
            self.segments.append(segment)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            previous_seg = self.segments[seg - 1].pos()
            self.segments[seg].goto(previous_seg)
        self.segments[0].forward(20)

    def add_segment(self):
        segment = t.Turtle()
        segment.up()
        segment.goto(self.segments[-1].pos())
        segment.shape("square")
        segment.color("white")
        self.segments.append(segment)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
