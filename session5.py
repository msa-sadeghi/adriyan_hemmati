import turtle

wn = turtle.Screen()
wn.title('My Turtle Program')
wn.bgcolor('lightpink')
# wn.register_shape('blue.gif')
t = turtle.Turtle()
# t.shape('blue.gif') # 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
t.shape("turtle")
t.color("green")
t.shapesize(3)
t.pencolor("red")
t.pensize(3)
t.speed("slowest")

sides = int(wn.textinput("sides", "چند ضلعی بکشم؟"))

for i in range(sides):
    t.forward(100)
    t.left(360/sides)

turtle.done()