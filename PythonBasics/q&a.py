# List vs Tuple
my_list = [1, 2, 3]
my_list[0] = 100
my_list.append(4)
my_list.pop(0)
print(my_list)

my_tuple = (1, 2, 3)
print(my_tuple)

# Data Types
x = 10 #int
y = 3.14 #float
z = "Hello, World!" #string
w = True #boolean
d = {"key": "value"} #dictionary

# Inheritance, inherits from the parent class
class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + " barks"
dog = Dog("Duke")
print(dog.speak())  # Output: Duke barks

#List of dictionaries
data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}]
my_dict = {"name": "Alice", "age": 30}
print(data)  # Output: [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
print(data[0]["name"])  # Output: Alice
print(data[1]["age"])  # Output: 25