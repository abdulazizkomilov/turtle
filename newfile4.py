import turtle
t = turtle.Turtle()
t.width(2)

def shape_wh(tur):
	if tur % 3 == 0:
		return "red"
	elif tur % 3 == 1:
		return "green"
	else:
		return "blue"

def shapes(tur):
	tur.right(75)
	for side in range(12):
		tur.forward(10)
		tur.left(30)
		tur.left(75)

t.penup()
t.back(150)
t.pendown()

for n in range(10):
	t.color(shape_wh(n))
	shapes(t)
	t.forward(40)