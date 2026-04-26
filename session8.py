import turtle as t

my_turtle = t.Turtle()
my_turtle.shape('turtle')
# my_turtle.speed('fastest')

numbers = [10, 20, 30, 40 ,50]
colors = ["black", "purple", "orange", "red", "blue"]
i = 0
for n in numbers:
    my_turtle.home()
    my_turtle.pencolor(colors[i])
    my_turtle.right(n * 3)
    my_turtle.forward(n * 3)
    i = i + 1


# for i in range(30):
#     my_turtle.pencolor(colors[i % 5])
#     my_turtle.color(colors[i % 5])
#     my_turtle.begin_fill()
#     for i in range(5):
#         my_turtle.forward(150)
#         my_turtle.right(144)
#     my_turtle.end_fill()
#     my_turtle.right(12)


t.done()