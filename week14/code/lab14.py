#CS 101 Lab
#Program 14
#John Chirpich
#jwcgnq@umkc.edu
import turtle
class Point(object):
    def __init__(self, x, y, color):
	    self.x = x
	    self.y = y
	    self.color = color
    def draw(self):
	    turtle.penup()
	    turtle.goto(self.x, self.y)
	    turtle.pendown()
	    turtle.pencolor(self.color)
	    turtle.setheading(0)
	    self.draw_action()
    def draw_action(self):
	    turtle.dot()
class box(Point):
	def __init__(self, x, y, width, height, color):
		self.width = width
		self.height = height
		super().__init__(x, y, color)
	def draw_action(self):
		turtle.forward(self.width)
		turtle.right(90)
		turtle.forward(self.height)
		turtle.right(90)
		turtle.forward(self.width)
		turtle.right(90)
		turtle.forward(self.height)
		turtle.end_fill()
class boxFilled(box):
	def __init__(self, x, y, width, height, color, filcolor):
		self.filcolor = filcolor
		super().__init__(x, y,width, height, color)
		self.fill_it()
	def fill_it(self):
		print(self.filcolor)
		turtle.fillcolor(self.filcolor)
		turtle.begin_fill()
class Circle(Point):
	def __init__(self, x, y, color, radius):
		turtle.pencolor(color)
		turtle.circle(radius)
		super().__init__(x, y)
class CircleFilled(Point):
	def __init__(self, x, y, color, radius, FillingColor):
		turtle.pencolor(color)
		turtle.fillcolor(FillingColor)
		turtle.begin_fill()
		turtle.circle(radius)
		turtle.end_fill()
		super().__init__(x, y)
