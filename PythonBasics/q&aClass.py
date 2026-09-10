class MyClass:
    @classmethod
    def class_method(cls):
        return "Class method called"

    def instance_method(self):
        return "Instance method called"

obj = MyClass()

print(MyClass.class_method()) #Class method called, can be accessed without creating an instance of the class

print(obj.instance_method())  #Instance method called