# def hello(name):
#     print(f"Hello {name}")


# hello("sara")
# hello("reza")

# def add(a,b):
#     return a + b

# print(add(1,2))

import random
def gramer_name(name):
    words = ["Destroyer", "Shadow", "ninja", "Storm", "Hunter"]
    return name + "_" + random.choice(words)

print(gramer_name("Arman"))