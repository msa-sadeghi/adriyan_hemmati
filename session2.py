# name = input("enter your name ")
# print("hello", name)

# number1 = float(input("enter first  number: "))
# number2 = float(input("enter second  number: "))

# print("div of two numbers: ", number1 // number2)


# age_text = input("how old are you? ")
# age = int(age_text)  # تبدیل رشته به عدد صحیح
# days = age * 365
# print("you lived", days)


# height_text = input("enter your height in meter: ")
# height = float(height_text)
# print("your height in cm: ", height * 100)


first_number = int(input("enter a number: "))
second_number = int(input("enter a number: "))
op = input("enter (+ - * /):  ")
if op == "+":
    print("calculation result")
    print("sum is:", first_number + second_number)
elif op == "-":
    print("calculation result")
    print("sub is:", first_number - second_number)
elif op == "*":
    print("calculation result")
    print("Mul is:", first_number * second_number)
elif op == "/":
    print("calculation result")
    print("Div is:", first_number / second_number)
else:
    print("operation is not valid")
print("end of program")