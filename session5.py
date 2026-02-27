import turtle

wn = turtle.Screen()
wn.title('My Turtle Program')
wn.bgcolor('lightpink')
wn.register_shape('blue.gif')
t = turtle.Turtle()
t.shape('blue.gif') # 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
t.color("green")
t.shapesize(3)
turtle.done()