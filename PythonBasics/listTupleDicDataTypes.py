values = [1, 2, "Mel", 2.4]
# List is a data type that allows multiple values of different type
print(values)
print(type(values))
print(values[2])
# Last index
print(values[-1])
# extract a sub list
print(values[1:3])
# extract sub index
values.insert(3, "B")
print(values)

# add value to the end
values.append("A")
print(values)

# update a value
values[2] = "C"
print(values)
# delete
del values[0]
print(values)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Fruits from index 1 to 2:", fruits[1:3])


# Tuple - Same as list but not immutable
val = (1, 2, "Mel", 2.4)
print(val[1])
# val[2] = "C"
# print(val)
person = ("Rahul", 25, 5.9)
print("Age:", person[1])

# Dictionary
dic = {"a":2, 4:"bcd", "c":"Hello World"}
print(dic[4])
print(dic["c"])

# Insert values
dic = {}

dic["firstName"] = "John"
dic["lastName"] = "Doe"
dic["gender"] = "Male"

print(dic)
print(dic["firstName"])

car = {"make": "Toyota", "model": "camry", "year": 2020, "color": "Blue"}
car["owner"] = "Rahul"
car["model"] = "Camry"

print("Car model:", car["model"])
print("Updated car dictionary:", car)