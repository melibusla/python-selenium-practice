# file = open("test.txt")
#
# file.close()

#open and closes it // also a parameter states if it reads "r" or "w" for "write"
with open("test.txt", "r") as reader:
    content = reader.readlines()
    reversed(content)
    with open("test.txt", "w") as writer:
        for line in reversed(content):
            writer.write(line)

with open("test.txt", "r") as reader:
    content = reader.read()
    print(content)


#---------------------------
countLine = 0
with open ("file1.txt", "r") as reader:
    content = reader.readlines()
    for line in content:
        countLine = countLine+1
    print("Total number of lines:", countLine)
#------official
with open('file1.txt', 'r') as file:
    count = sum(1 for line in file)
    print(f'Total number of lines: {count}')