import turtle
def balloon(t, color):
	t.color(color)
	for side in range(30):
		t.forward(10)
		t.left(12)
	t.right(60)
	for side in range(3):
		t.forward(10)
		t.right(120)
	t.color("gray")
	t.right(30)
	t.forward(100)

t = turtle.Turtle()
t.penup()
t.back(100)
t.pendown()
balloon(t, "red")
t.penup()
t.home()
t.pendown()
balloon(t, "blue")
t.penup()
t.home()
t.forward(100)
t.pendown()
balloon(t, "purple")
t.mainloop()