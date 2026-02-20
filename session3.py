# age = int(input("enter the number: "))
# if age >= 18:
#     print("you can drive")
#     print("welcome to adult world")


# score = int(input("Enter score between 0 - 20 "))

# if score >= 18:
#     print("A")
# elif score >= 15:
#     print("B")
# elif score >= 10:
#     print("C")
# else:
#     print("you failed")


# age = 25
# has_license = True

# if age >= 18 and has_license == True:
#     print("you can drive   ")


# day = "sat"

# if day == "sat" or day == "sun":
#     print("we can go out...")


# is_raining = False

# if not is_raining:
#     print("we can go park !")


print("=== Welcome to Mellat Park ===")
print("We will check the conditions for riding the roller coaster...\n")

age = int(input("How old are you? "))
height = int(input("What is your height in centimeters? "))

# Check main conditions
if age < 12:
    print(" Sorry, you are too young!")
elif height < 140:
    print(" Sorry, your height is not enough!")
else:
    print(" You can ride!")
    
    # Calculate ticket price based on age
    if age < 18:
        price = 50000
        print("Teen ticket price:", price, "Tomans")
    elif age >= 60:
        price = 30000
        print("Senior ticket price:", price, "Tomans")
    else:
        price = 70000
        print("Adult ticket price:", price, "Tomans")
