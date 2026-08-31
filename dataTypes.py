print("Hello")

# comment line
a = 1
b = 2
print(a)
Str = "Hello!!!"
c, d, e = 1, 2.4, "Sample"
# print(Str, c, e)

# print("{} {}".format("Value is", b))
#
# print(type(b))
# print(type(c))
# print(type(e))

InstructorName = "Rahul!"

greeting = "Welcome to Python Programming"
print(greeting)
# greeting = ("{} {}".format("Welcome to Python Programming,", InstructorName))
greeting = ("Welcome to Python Programming," + InstructorName)
print(greeting)

age, height, favorite_color = 25, 5.9, "blue"
# En el curso dicen que no se pueden concatenar 2 types diferentes, asi que se usa format, pero con , funciona bien o.O
print("{} {} {} {} {} {} {} {} {} {} {} {} {} {} {}".format("Age:", age, "|", "Type:", type(age), "Height:", height, "|", "Type:", type(height), "Favorite Color:", favorite_color, "|", "Type:", type(favorite_color)))

print("Age:", age, "|", "Type:", type(age), "Height:", height, "|", "Type:", type(height), "Favorite Color:", favorite_color, "|", "Type:", type(favorite_color))

print("Variable a is:", age)