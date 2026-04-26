# numbers = (1,2,3,4,5)
# for n in numbers:
#     print(n)

# student_age = {
#     "ali" : 32,
#     "sara":15
# }
# student_age["ali"] = 12
# del student_age["sara"]
# print(student_age["ali"])
# print(student_age)

# favorite_sport = {
#     "sara" : "football",
#     "reza" : "tennis",
#     "matin" : "football"
# }

# print(f"reza likes {favorite_sport['reza']}")
# print(f"reza likes {favorite_sport.get("sara")}")
# favorite_sport["mary"] = "basketball"
# print(favorite_sport)

# favorite_sport = {
#     "sara" : "football",
#     "reza" : "tennis",
#     "matin" : "football"
# }


# for sport in favorite_sport:
#     print(sport)
# print("++++++++++++++++++++++")
# for sport in favorite_sport.values():
#     print(sport)
# print("++++++++++++++++++++++")
# for key, val in favorite_sport.items():
#     print(key, val)



# student_age = {
#     "ali" : 12,
#     "sara":30,
#     "mary" : 7
# }

# sum_of_ages = 0
# for age in student_age.values():
#     sum_of_ages += age
# print("sum of student's ages :", sum_of_ages)


# name = input("enter a name: ")
age = int(input("enter the age : "))
if age > 18:
    print("Adult")
else:
    print("Teenager")


