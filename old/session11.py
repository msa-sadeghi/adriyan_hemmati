# def welcome_user(name, age):
#     return f"welcome {name}, you are {age} years old"


# print(welcome_user("sara", 17))

# def max_number(a,b):
#     if a > b:
#         return a
#     else:
#         return b

# print(max_number(12, 9))

def repeat_word(w, n):
    for i in range(n):
        print(w)

repeat_word("hi", 4)
import random
samples = ["King", "Warrior", "Ghost", "Dragon"]
def random_name(name):
    return f"{name}_{random.choice(samples)}"

print(random_name("ali"))