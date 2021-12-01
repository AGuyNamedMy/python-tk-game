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

def returnFunction():
    if top.xcor() > 290 or top.xcor() < -290 or top.ycor() > 290 or top.ycor() < -290:
        global eaten
        global delay
        global segments
        time.sleep(1)
        top.goto(0, 0)
        top.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        eaten = 0
        delay = 0.1
        return eaten
        return delay
        return segments

def eating():
    if top.distance(food) < 20:
        global segments
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)  
        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        global delay
        global eaten
        delay -= 0.001
        eaten += 10
        return delay
        return eaten
        return segments

def segmentCollision():
    global segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = top.xcor()
        y = top.ycor()
        segments[0].goto(x, y)
        
    return segments
def bodycollision():
    for segment in segments:
        if segment.distance(top) < 20:
            time.sleep(1)
            top.goto(0, 0)
            top.direction = "stop"
            colors = randomStuff.randomColors
            shapes = randomStuff.randomShapes
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            eaten = 0
            delay = 0.1
            return segments
            return eaten
            return delay
#-----events--------------

wn.listen()
wn.onkeypress(characterctrl.goup, "w")
wn.onkeypress(characterctrl.godown, "s")
wn.onkeypress(characterctrl.goleft, "a")
wn.onkeypress(characterctrl.goright, "d")
  
segments = []
  

  
# Main Gameplay
while True:
    wn.update()
    returnFunction()
    eating()
    # Checking for top collisions with body segments
    segmentCollision()
    characterctrl.move()
    bodycollision()
    time.sleep(delay)