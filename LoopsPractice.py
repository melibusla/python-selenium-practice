# If
greeting = "Hello"

if greeting == "Well Hello":
    print("Condition matches")
else:
    print("Condition do not match")
#     identation matters
print("if else condition code is completed")

a = 1
b = 2

if a > 2:
    print("a is greater than 2")
else:
    print("a is not greater than 2")

greeting = "Hello"
if greeting == "Hello":
    print("Hello there!")
    print("How can I assist you today?")
else:
    print("Greetings!")
print("Program has completed.")

b = 15
if b > 10:
    print("Number is greater than 10")
else:
    print("Number is 10 or less.")
print("Comparison code is completed.")
# for

obj= [1, 4, 5, 6, 7]
# for i in obj:
#     print(i)
#
# for i in obj:
#     print(i*2)
numbers = [1, 4, 7, 10]
for i in numbers:
    print(i*3)
#  Sum of first natural numbers 1+2+3+4+5 = 15
# range (i, j) => i to j-1
summation = 0
# summation = summation +j
for j in range(1, 6):
    summation += j
    print(j)
print(summation)
print("++++++++++++++Iteration count++++++++++++++++")
for k in range(1, 10, 2):
    print(k)
print("++++++++++++Skipping first index++++++++++++++++++")
for m in range(10):
    print(m)

#  While
print("While")
it = 10

while it>1:
    if it == 9:
        it = it-1
        continue
    if it == 3:
        break
    print(it)

    it = it-1

print("While loop is done")