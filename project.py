# imports
import turtle
import time
import random

#-----global configuration----
wn = turtle.Screen()
wn.title("game")
wn.setup(width=600, height=600)

#--classes--


class food:
    food = turtle.Turtle()
    food.speed(0)
    food.shape('circle')
    food.color('red')
    food.penup()
    food.goto(0, 100)


#character attrebutes like shape and color
class characterAttr:
    shape = 'square'
    head = turtle.Turtle()
    segments = []
    delay = 0.1
    eaten = 0

class characterbehavior(characterAttr):
    def start_function(self):
        shape = self.shape
        self.head.shape(shape)
        self.head.penup()
        self.head.goto(0, 0)
        self.head.direction = "Stop"
    def bodycollision(self):
        for segment in self.segments:
            if segment.distance(self.head) < 20:
                time.sleep(1)
                self.head.goto(0, 0)
                self.head.direction = "stop"
                #colors = randomStuff.randomColors
                #shapes = randomStuff.randomShapes
                for segment in self.segments:
                    segment.goto(1000, 1000)
                self.segments.clear()
                self.eaten = 0
                self.delay = 0.1
    def segmentCollision(self):
        for index in range(len(self.segments)-1, 0, -1):
            x = self.segments[index-1].xcor()
            y = self.segments[index-1].ycor()
            self.segments[index].goto(x, y)
        if len(self.segments) > 0:
            x = self.head.xcor()
            y = self.head.ycor()
            self.segments[0].goto(x, y)
    def adding_segments(self):
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color("orange")  # tail colour
        new_segment.penup()
        self.segments.append(new_segment)
        self.delay -= 0.001
        self.eaten += 10
    def eating(self):
        if self.head.distance(food.food) < 20:
            food.food.goto(random.randint(-270, 270), random.randint(-270, 270))
            food.food.shape(random.choice(['square', 'triangle', 'circle']))
            food.food.color(random.choice(['orange', 'yellow', 'purple', 'blue']))  
            # Adding segment
            self.adding_segments()
    def returnFunction(self):
        if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -290:
            time.sleep(1)
            self.head.goto(0, 0)
            self.head.direction = "Stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in self.segments:
                segment.goto(1000, 1000)
            self.segments.clear()
            self.eaten = 0
            self.delay = 0.1

# character controls and movements    
class characterctrl(characterAttr):
    def goup(self):
        if self.head.direction != "down":
            self.head.direction = "up"
    def godown(self):
        if self.head.direction != "up":
            self.head.direction = "down"
    def goleft(self):
        if self.head.direction != "right":
            self.head.direction = "left"
    def goright(self):
        if self.head.direction != "left":
            self.head.direction = "right"
    def move(self):
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y+20)
        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y-20)
        if self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x-20)
        if self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x+20)
    def keybindings(self):
        wn.listen()
        wn.onkeypress(self.goup, "w")
        wn.onkeypress(self.godown, "s")
        wn.onkeypress(self.goleft, "a")
        wn.onkeypress(self.goright, "d")
       # wn.onkeypress(change_loop_number(loop_number), "q")


class character_class(characterbehavior, characterctrl):
    pass
    

character = character_class()

#-----events--------------
character.start_function()
character.keybindings()  
# Main loop
while True:
    wn.update()
    character.returnFunction()
    character.eating()
    # Checking for head collisions with body segments
    character.segmentCollision()
    character.move()
    character.bodycollision()
    time.sleep(character.delay)