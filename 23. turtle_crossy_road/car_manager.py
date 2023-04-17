from turtle import Turtle
import random

COLORS = ['red', 'blue', 'green', 'yellow', 'black', 'brown', 'purple', 'orange']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(1, 2)
        self.color(random.choice(colors))
        self.setheading(180)
        self.goto(random.randint(-10, 300), random.randint(-240, 300))

    def generate_cars(self):
        for _ in range(60):
            cars.append(self)

    def move(self):
        self.setheading(180)
        self.forward(2)

    def random_cars(self):
        pos_x = 300
        random_y = random.randint(-260, 300)
        self.goto(pos_x, random_y)
        self.setheading(180)
        self.forward(2)

    # def color
    # color = list(np.random.choice(range(256), size=3))


