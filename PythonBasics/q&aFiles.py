with open("test.txt","w") as f:
    f.write("Hello World")

try:
    with open("test.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError as e:
    print(f"File not found. Please check the file path. Error: {e}")
finally:
    print("Execution completed.")

with open("test.txt", "r") as f:
    content = f.read()
    print(content)