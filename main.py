#   a123_apple_1.py
import turtle as trtl
import random

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image) 

drawer = trtl.Turtle()
apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
  
letters = ["a", "b", "c", "d", "e", "f"]
def make_turtles():
  turtles = []
  for _ in range(3):
    t = trtl.Turtle()
    t.penup()
    draw_apple(t)
    t.goto(random.randint(-100, 100), random.randint(-10, 90))
    turtles.append(t)
  return turtles

def draw_letters(letters, turtles):
  drawers = []
  for i, turtle in enumerate(turtles):
    drawer = trtl.Turtle()
    drawer.penup()
    drawer.hideturtle()
    drawer.goto(turtle.xcor()-18, turtle.ycor()-35)
    drawer.write(letters[i], font=("Arial", 40, "bold"))
    drawers.append(drawer)
  return drawers
  

def draw_an_A(drawer):
  drawer.hideturtle()
  drawer.goto(-10, -40)
  drawer.color("white")
  drawer.write("A", font=("Arial", 40, "bold"))

def erase_an_A():
  global drawer
  drawer.clear()

def apple_fall():
  global apple
  x = apple.xcor()
  y = apple.ycor()
  apple.penup()
  apple.goto(x, y-140)
  erase_an_A()
 
#-----function calls-----
apples = make_turtles()
draw_letters(letters, apples)
wn.onkeypress(apple_fall, "a")

wn.listen()
wn.mainloop()