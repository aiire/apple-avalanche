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

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
	active_apple.shape(apple_image)
	wn.update()
  
letters = ["a", "s", "d", "f"]
def make_apple_turtles():
	turtles = []
	for _ in range(len(letters)):
		t = trtl.Turtle()
		t.penup()
		draw_apple(t)
		t.goto(random.randint(-100, 100), random.randint(-10, 90))
		turtles.append(t)
	return turtles

def draw_letter(x, y, drawer, letter):
	drawer.goto(x, y)
	drawer.color("white")
	drawer.write(letter.upper(), font=("Arial", 40, "bold"))

def draw_letters(letters, turtles):
	drawer_turtles = []
	for i, letter in enumerate(letters):
		drawer = trtl.Turtle()
		drawer.penup()
		drawer.hideturtle()
		turtle = turtles[i]
		draw_letter(turtle.xcor()-10, turtle.ycor()-40, drawer, letter)
		drawer_turtles.append(drawer)
	return drawer_turtles
  

# def draw_an_A(drawer):
#   drawer.hideturtle()
#   drawer.goto(-10, -40)
#   drawer.color("white")
#   drawer.write("A", font=("Arial", 40, "bold"))

# def erase_an_A():
#   global drawer
#   drawer.clear()




def erase_letter(index):
	global drawer_turtles
	drawer = drawer_turtles[index]
	drawer.clear()

def apple_fall(index):
	turtle = apple_turtles[index]
	drawer = drawer_turtles[index]
	letter = letters[index]
	x = turtle.xcor()
	y = turtle.ycor()
	turtle.penup()
	turtle.goto(x, y-140)
	erase_letter(index)
	draw_letter(turtle.xcor()-10, turtle.ycor()-40, drawer, letter)

#-----function calls-----
apple_turtles = make_apple_turtles()
drawer_turtles = draw_letters(letters, apple_turtles)

wn.onkeypress(lambda: apple_fall(0), 'a')
wn.onkeypress(lambda: apple_fall(1), 's')
wn.onkeypress(lambda: apple_fall(2), 'd')
wn.onkeypress(lambda: apple_fall(3), 'f')

wn.listen()
wn.mainloop()