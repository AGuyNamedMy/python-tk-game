# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
#-----game configuration----


#-----initialize turtle-----
wn = trtl.Screen()
wn.screensize()
trtl.penup()

#-----game functions------

#pacman controls keybindings
def up():
    trtl.setheading(90)
    trtl.forward(10)
def left():
    trtl.setheading(180)
    trtl.forward(10)
def right():
    trtl.setheading(0)
    trtl.forward(10)
def down():
    trtl.setheading(270)
    trtl.forward(10)


def keybindings():
    trtl.onkey(up, "k")
    trtl.onkey(left, "h")
    trtl.onkey(right, "l")
    trtl.onkey(down, "j")

def character():
    trtl.shape("circle")

#main function
def main():
    character()
    keybindings()       
    trtl.listen()
    trtl.exitonclick()
#-----events--------------
main()