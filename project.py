# imports
import turtle
import time
import random

#-----global configuration----
wn = turtle.Screen()
wn.title("game")
wn.setup(width=600, height=600)



#--classes--


#randomisation
class randomStuff:
    randomShapes = random.choice(['square', 'triangle', 'circle'])
    randomColors = random.choice(['red', 'green', 'black'])
    randomX = random.randint(-270, 270)
    randomY = random.randint(-270, 270)

class food:
    def food_init():
        food = turtle.Turtle()
        food.speed(0)
        food.shape(randomStuff.randomShapes)
        food.color(randomStuff.randomColors)
        food.penup()
        food.goto(0, 100)


#character attrebutes like shape and color
class characterAttr:
    shape = randomStuff.randomShapes
    top = turtle.Turtle()
    def start_function(self):
        self.top.shape(self.shape)
        self.top.penup()
        self.top.goto(0, 0)
        self.top.direction = "Stop"

# character controls and movements    
class characterctrl(characterAttr):
    def goup(self):
        if self.top.direction != "down":
            self.top.direction = "up"
    def godown(self):
        if self.top.direction != "up":
            self.top.direction = "down"
    def goleft(self):
        if self.top.direction != "right":
            self.top.direction = "left"
    def goright(self):
        if self.top.direction != "left":
            self.top.direction = "right"
    def move(self):
        if self.top.direction == "up":
            y = self.top.ycor()
            self.top.sety(y+20)
        if self.top.direction == "down":
            y = self.top.ycor()
            self.top.sety(y-20)
        if self.top.direction == "left":
            x = self.top.xcor()
            self.top.setx(x-20)
        if self.top.direction == "right":
            x = self.top.xcor()
            self.top.setx(x+20)
    def keybindings(self):
        wn.listen()
        wn.onkeypress(self.goup, "w")
        wn.onkeypress(self.godown, "s")
        wn.onkeypress(self.goleft, "a")
        wn.onkeypress(self.goright, "d")


class character(characterctrl):
    delay = 0.1
    eaten = 0
    segments = []


#-----functions------
# restarts when outside of window
def returnFunction():
    if top.xcor() > 290 or top.xcor() < -290 or top.ycor() > 290 or top.ycor() < -290:
        time.sleep(1)
        top.goto(0, 0)
        top.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])
        for segment in character.segments:
            segment.goto(1000, 1000)
        character.segments.clear()
        character.eaten = 0
        character.delay = 0.1

def eating():
    if top.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)  
        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")  # tail colour
        new_segment.penup()
        character.segments.append(new_segment)
        character.delay -= 0.001
        character.eaten += 10

def segmentCollision():
    for index in range(len(character.segments)-1, 0, -1):
        x = character.segments[index-1].xcor()
        y = character.segments[index-1].ycor()
        character.segments[index].goto(x, y)
    if len(character.segments) > 0:
        x = top.xcor()
        y = top.ycor()
        character.segments[0].goto(x, y)
def bodycollision():
    for segment in character.segments:
        if segment.distance(top) < 20:
            time.sleep(1)
            top.goto(0, 0)
            top.direction = "stop"
            colors = randomStuff.randomColors
            shapes = randomStuff.randomShapes
            for segment in character.segments:
                segment.goto(1000, 1000)
            character.segments.clear()
            character.eaten = 0
            character.delay = 0.1

#-----events--------------

# food in the game
character.start_function()

wn.listen()
wn.onkeypress(character.goup, "w")
wn.onkeypress(character.godown, "s")
wn.onkeypress(character.goleft, "a")
wn.onkeypress(character.goright, "d")
    
# Main loop
while True:
    wn.update()
    returnFunction()
    eating()
    # Checking for top collisions with body segments
    segmentCollision()
    character.move()
    bodycollision()
    time.sleep(character.delay)