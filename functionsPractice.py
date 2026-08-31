# function declaration

def GreetMe():
    print("Greetings")
GreetMe()

# function with parameters
def GreetMe(name):
    print("Greetings "+name)

GreetMe("Mel")

def addIntegers(a, b):
    print(a+b)

addIntegers(1, 2)

def addIntegers(a, b):
    return a+b

print(addIntegers(2, 2))

def custom_greeting(user):
    if 5 <= user <= 11:
        greeting = "Good Morning"
    elif 12 <= user <= 17:
        greeting = "Good Afternoon"
    elif 18 <= user <= 21:
        greeting = "Good Evening"
    else:
        greeting = "Good Night"
    return greeting + "\nGreeting code has completed."

print(custom_greeting(10))
print(custom_greeting(15))