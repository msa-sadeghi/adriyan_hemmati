class Student:
    def __init__(self,n, a):
        self.name = n
        self.age = a

    def move(self):
        print(f"{self.name} is moving")
    def speak(self):
        print(f"{self.name} is speaking")


s1 = Student("sara", 23)
s2 = Student("reza", 12)

print(s1.name)
print(s2.name)
s1.move()
s2.speak()