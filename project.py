# imports
import turtle
import time
import random

#-----global configuration----

delay = 0.1
eaten = 0

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

#character attrebutes like shape and color
class characterAttr:
    shape = randomStuff.randomShapes
# character controls and movements    
class characterctrl:
    def goup():
        if top.direction != "down":
            top.direction = "up"
    def godown():
        if top.direction != "up":
            top.direction = "down"
    def goleft():
        if top.direction != "right":
            top.direction = "left"
    def goright():
        if top.direction != "left":
            top.direction = "right"
    def move():
        if top.direction == "up":
            y = top.ycor()
            top.sety(y+20)
        if top.direction == "down":
            y = top.ycor()
            top.sety(y-20)
        if top.direction == "left":
            x = top.xcor()
            top.setx(x-20)
        if top.direction == "right":
            x = top.xcor()
            top.setx(x+20)

class character(characterAttr, characterctrl):
    delay = 0.1
    eaten = 0
    segments = []

top = turtle.Turtle()
top.shape(characterAttr.shape)
top.penup()
top.goto(0, 0)
top.direction = "Stop"

# food in the game
food = turtle.Turtle()
colors = randomStuff.randomColors
shapes = randomStuff.randomShapes
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

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

wn.listen()
wn.onkeypress(character.goup, "w")
wn.onkeypress(character.godown, "s")
wn.onkeypress(character.goleft, "a")
wn.onkeypress(character.goright, "d")
  
segments = []
  

  
# Main loop
while True:
    wn.update()
    returnFunction()
    eating()
    # Checking for top collisions with body segments
    segmentCollision()
    character.move()
    bodycollision()
    time.sleep(delay)