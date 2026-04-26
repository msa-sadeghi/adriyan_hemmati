# students_list = ["amir", "sara", "jaber"]
# print(len(students_list))
# students_list.append("adrian")
# print(students_list)
# print(len(students_list))
# print(students_list[0])
# print(students_list[3])
# print(students_list[-1])
# print(students_list[len(students_list) - 1])
# print("*" * 10)
# for s in students_list:
#     print(s)

# i = 0
# while i < len(students_list):
#     print(students_list[i])
#     i += 1




# all_prices = []

# for i in range(3):
#     price = float(input("enter the price: "))
#     all_prices.append(price)

# print("all prices:", all_prices)
# print("sum of prices:", sum(all_prices))


colors = ["red", "blue", "green", "purple", "red", "blue"]
print(len(colors))
new_colors = []
for c in colors:
    if c not in new_colors:
        new_colors.append(c)

print(new_colors)
print(len(new_colors))