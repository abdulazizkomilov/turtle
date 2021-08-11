import turtle
t = turtle.Turtle()
p = turtle.Turtle()

t.width(3)
t.color("red")

p.width(3)
p.color("red")

t.p = "shape"
t.left(40)
t.forward(100)
for side in range(185):
	t.forward(1)
	t.left(1)
t.hideturtle()

if t.p == "shape":
	p.left(140)
	p.forward(100)
	for side in range(185):
		p.forward(1)
		p.right(1)
p.hideturtle()

t.speed(0)
p.speed(0)
