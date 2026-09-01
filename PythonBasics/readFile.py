file = open("test.txt")
#read all the contents
# print(file.read())
#read characters by parameters
# print(file.read(2))
# print(file.read(5))
# read by length, single line
# print(file.readline())
# print(file.readline())

#print line by line using a method
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# each line will be stored in a list
for line in file.readlines():
    print(line)



file.close()