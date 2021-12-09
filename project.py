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
    segments = []
    delay = 0.1
    eaten = 0
    new_segment = turtle.Turtle()

class characterbehavior(characterAttr):
    def start_function(self):
        self.top.shape(self.shape)
        self.top.penup()
        self.top.goto(0, 0)
        self.top.direction = "Stop"
    def bodycollision(self):
        for segment in self.segments:
            if segment.distance(self.top) < 20:
                time.sleep(1)
                self.top.goto(0, 0)
                self.top.direction = "stop"
                colors = randomStuff.randomColors
                shapes = randomStuff.randomShapes
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
            x = self.top.xcor()
            y = self.top.ycor()
            self.segments[0].goto(x, y)
    def adding_segments(self):
        self.new_segment.speed(0)
        self.new_segment.shape("square")
        self.new_segment.color("orange")  # tail colour
        self.new_segment.penup()
        self.segments.append(self.new_segment)
        self.delay -= 0.001
        self.eaten += 10
    def eating(self):
        if self.top.distance(food.food) < 20:
            x = random.randint(-270, 270)
            y = random.randint(-270, 270)
            food.food.goto(x, y)  
            # Adding segment
            self.adding_segments()
    def returnFunction(self):
        if self.top.xcor() > 290 or self.top.xcor() < -290 or self.top.ycor() > 290 or self.top.ycor() < -290:
            time.sleep(1)
            self.top.goto(0, 0)
            self.top.direction = "Stop"
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


class mainclass(characterbehavior, characterctrl):
    rando = 0
    

character = mainclass()

#-----events--------------

# food in the game
character.start_function()
character.keybindings()
   
# Main loop
while True:
    wn.update()
    character.returnFunction()
    character.eating()
    # Checking for top collisions with body segments
    character.segmentCollision()
    character.move()
    character.bodycollision()
    time.sleep(character.delay)