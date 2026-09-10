import asyncio

import pytest
import time

# @pytest.fixture
# def sample_data():
#     print("\nSetup: Creating test data") #Runs before the test
#     data = {"name": "Alice", "age": 30}
#     # return data # provides the data to the test function
#     yield data # provides the data to the test function and allows for teardown after the test
#     print("\nTeardown: Cleaning up test data") # Runs after the test
#
# def test_example(sample_data):
#     assert sample_data["name"] == "Alice"
#     assert sample_data["age"] == 30
#     print("Test executed with sample data:", sample_data)

# def add(a, b):
#     return a + b
# addLambda = lambda x, y : x + y
#
numbers = [1, 2, 3, 4, 5]
#map
squared_numbers = list(map(lambda x: x**2, numbers))
multiplied_numbers = list(map(lambda x: x*2, numbers))
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
print("Multiplied numbers:", multiplied_numbers)

#filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

#sorting
num = [15, 8, 6, 23, 42, 4]
print("Original list:", num)
# Sort in ascending order
print(sorted(num))
# Sort in descending order
print(sorted(num, reverse=True))
print(numbers[::-1])  # Reverse the list using slicing

# def task(name):
#     print(f"Starting {name}")
#     time.sleep(2)
#     print(f"Finished {name}")
#
# task("Task 1")
# task("Task 2")
#
# async def task(name):
#     print(f"Starting {name}")
#     await asyncio.sleep(2)
#     print(f"Finished {name}")
#
# async def main():
#     await asyncio.gather(
#         task("Task 1"),
#         task("Task 2")
#     )
# asyncio.run(main())