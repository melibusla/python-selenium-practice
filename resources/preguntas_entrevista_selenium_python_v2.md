# Interview Questions — Section 23, Selenium + Python (Rahul Shetty Academy)

> How to fill each block:
> 1. **Short answer, in your own words** — what you'd say out loud in an interview, not the course's textbook definition.
> 2. **Example code** — only if it applies, adapted, not the full block from the video.
> 3. **Connection to my repo** — e.g. "I used this in `conftest.py` for the browser flag." If it doesn't apply, leave it as "N/A — haven't used this yet," don't force it.

---

## Block 1 — Python core (types, structures, functions)

### 00:00 — What is the difference between a list and a tuple?

- **Short answer:** Lists are mutable (you can add, remove, or change elements after creation); tuples are immutable (once created, they can't be changed). Both are ordered and allow duplicates.
- **Code:**
```python
my_list = [1, 2, 3]
my_list[0] = 100
my_list.append(4)
my_list.pop(0)
print(my_list)          # [100, 2, 3, 4] -> after edits: [2, 3, 4]

my_tuple = (1, 2, 3)
print(my_tuple)          # (1, 2, 3) - can't reassign my_tuple[0]
```
- **Connection to my repo:** N/A — haven't needed to explain this distinction in code, but your test data (loaded from JSON) comes in as lists of dicts, which are mutable — worth mentioning if asked why you didn't use tuples for test data.

### 05:04 — What are Python's built-in data types?

- **Short answer:** Python groups them into: numeric (`int`, `float`, `complex`), sequence (`str`, `list`, `tuple`, `range`), mapping (`dict`), set types (`set`, `frozenset`), boolean (`bool`), and `NoneType`.
- **Code:**
```python
x = 10          # int
y = 3.14        # float
z = "Hello!"    # str
w = True        # bool
d = {"key": "value"}   # dict
lst = [1, 2, 3]        # list
tup = (1, 2, 3)        # tuple
s = {1, 2, 3}          # set
n = None               # NoneType
```
- **Connection to my repo:** Your JSON test data is parsed into Python's `dict` and `list` types automatically — every parametrized test case is a `dict` inside a `list`.

### 15:16 — How do you read and write files in Python?

- **Short answer:** Use the built-in `open()` function with a mode (`"r"` read, `"w"` write/overwrite, `"a"` append), ideally inside a `with` block so the file closes automatically even if an error happens.
- **Code:**
```python
with open("test.txt", "w") as f:
    f.write("Hello World")

with open("test.txt", "r") as f:
    content = f.read()
    print(content)
```
- **Connection to my repo:** You read test data from JSON files (`json.load()` on a file opened with `with open(...)`), and your framework writes pytest-html reports and failure screenshots to disk — same underlying pattern.

### 25:51 — How do you create a list of dictionaries in Python?

- **Short answer:** It's a list where each element is a dict — a common way to represent structured records like rows of data, and exactly how JSON arrays of objects map into Python.
- **Code:**
```python
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
print(data[0]["name"])   # Alice
print(data[1]["age"])    # 25
```
- **Connection to my repo:** This is exactly the shape of your data-driven tests. Your JSON test data file is a list of dicts, and `@pytest.mark.parametrize` iterates over that list to run one test per entry.

### 30:32 — What is a lambda function in Python?

- **Short answer:** A small, anonymous, one-line function that can take multiple arguments but only has a single expression (no `return` keyword needed — the expression's result is returned automatically). Best for short, throwaway logic; use a regular `def` function if the logic needs more than one line or you want to reuse/name it.
- **Code:**
```python
def add(a, b):
    return a + b

add_lambda = lambda x, y: x + y
print(add_lambda(2, 3))   # 5
```
- **Connection to my repo:** N/A — haven't used lambdas in the framework yet.

### 33:46 — How does the lambda function apply to map() & filter() functions?

- **Short answer:** `map()` applies a lambda to every item in an iterable and returns a new iterable with the results. `filter()` applies a lambda that returns `True`/`False` to every item, and keeps only the items where it's `True`.
- **Code:**
```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25]
print(even_numbers)     # [2, 4]
```
- **Connection to my repo:** N/A — haven't used `map()`/`filter()` in the framework yet.

### 41:42 — How do you sort a list in Python?

- **Short answer:** Two options: `sorted(list)` returns a **new** sorted list and leaves the original untouched; `list.sort()` sorts the list **in place** and returns `None`. Both accept `reverse=True` for descending order.
- **Code:**
```python
num = [15, 8, 6, 23, 42, 4]

print(sorted(num))              # [4, 6, 8, 15, 23, 42] - new list
print(sorted(num, reverse=True)) # [42, 23, 15, 8, 6, 4]

num.sort()                      # modifies num itself
print(num)                      # [4, 6, 8, 15, 23, 42]
```
- **Connection to my repo:** N/A — haven't needed to sort test data or results in the framework yet.

### 43:07 — Is Python asynchronous or synchronous? What is the default type, and what is asyncio?

- **Short answer:** Python is synchronous by default — it executes code line by line, blocking, and each operation must finish before the next one starts. Python also supports asynchronous execution through the `asyncio` library, which lets you run non-blocking tasks: instead of waiting for one task to finish before starting the next, multiple tasks can run concurrently while waiting on I/O (like network calls).
- **Code:**
```python
import time
import asyncio

# Synchronous version
def sync_task(name):
    print(f"Starting {name}")
    time.sleep(2)
    print(f"Finished {name}")

sync_task("Task 1")
sync_task("Task 2")

# Asynchronous version
async def async_task(name):
    print(f"Starting {name}")
    await asyncio.sleep(2)
    print(f"Finished {name}")

async def main():
    await asyncio.gather(async_task("Task 1"), async_task("Task 2"))

asyncio.run(main())
```
- **Connection to my repo:** N/A — Selenium's standard WebDriver calls are synchronous/blocking, and your framework doesn't use `asyncio`.

### 55:46 — How do you reverse the elements of a list?

- **Short answer:** The most common way is slicing with `[::-1]`, which returns a new reversed list. You can also use `list.reverse()` to reverse in place, or `list(reversed(my_list))`.
- **Code:**
```python
numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])   # [5, 4, 3, 2, 1] - new list

numbers.reverse()      # reverses in place
print(numbers)         # [5, 4, 3, 2, 1]
```
- **Connection to my repo:** N/A — haven't needed to reverse a list in the framework yet.

### 01:06:25 — What is the Python "with" statement designed for?

- **Short answer:** The `with` statement is used for managing resources (like files, database connections, or WebDriver sessions) that need proper setup and cleanup. It guarantees the resource is closed/released automatically — even if an exception happens inside the block — without you having to write manual `try/finally` or explicit `.close()` calls.
- **Code:**
```python
with open("myfile.txt", "w") as file:
    file.write("Hello World")
# file is automatically closed here, even if write() raised an error
```
- **Connection to my repo:** You use `with open(...)` when loading your JSON test data files.

### 01:08:07 — How to handle exceptions in Python? Where does the finally keyword come into play?

- **Short answer:** Wrap risky code in a `try` block, catch specific exception types with `except`, and optionally use `finally` for code that must run no matter what — whether the `try` block succeeded, failed, or even if you catch and re-raise the exception. `finally` is commonly used for cleanup (closing files, quitting a browser session).
- **Code:**
```python
try:
    with open("test.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError as e:
    print(f"File not found. Please check the file path. Error: {e}")
finally:
    print("Execution completed.")
```
- **Connection to my repo:** This connects directly to a real bug you hit: `StaleElementReferenceException`. Storing a `WebElement` reference in `__init__` and reusing it after the DOM changes causes staleness — the fix was to re-query the element by its locator at the point of use rather than reusing a stored reference. You could describe wrapping that kind of interaction in a `try/except StaleElementReferenceException` with a retry, or explain how you avoided it altogether by re-querying.

---

## Block 2 — OOP (classes, inheritance, conventions)

### 06:27 — How do you implement inheritance and the super keyword in Python?

- **Short answer:** A class inherits from another by passing the parent class in parentheses: `class Dog(Animal):`. This gives the child class access to the parent's methods and attributes. `super()` lets the child call the parent's version of a method (e.g., to extend it instead of fully overriding it).
- **Code:**
```python
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return super().speak() + " and Dog barks"

dog = Dog()
print(dog.speak())  # Animal speaks and Dog barks
```
- **Connection to my repo:** N/A for now — worth checking whether your `pages/` folder has a shared base page class that other page classes inherit from (e.g., common `find_element`/wait helpers). If not, this is a possible improvement for the framework rather than something to claim as "done."

### 10:37 — What is __init__() in Python?

- **Short answer:** `__init__()` is the constructor method — it runs automatically whenever a new instance of a class is created, and it's where you initialize the object's starting state (its attributes).
- **Code:**
```python
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " barks"

dog = Dog("Duke")
print(dog.speak())  # Duke barks
```
- **Connection to my repo:** This is core to your POM structure — each page class's `__init__(self, driver)` stores `self.driver = driver` so every method on that page object can use the same WebDriver instance.

### 52:07 — Why is the "self" convention used in Python? Explain with an example.

- **Short answer:** `self` refers to the current instance of the class and must be the first parameter of any instance method — though you don't pass it explicitly when calling the method, Python does that for you. Unlike Java or C++, which have an implicit `this`, Python requires `self` to be written explicitly so instance variables and methods stay clearly tied to a specific object.
- **Code:**
```python
class Page:
    def __init__(self, driver):
        self.driver = driver   # self ties "driver" to this specific instance

    def open(self, url):
        self.driver.get(url)   # accessing the instance's own driver
```
- **Connection to my repo:** Every method in your Page Object classes uses `self.driver` to call the shared WebDriver instance for that page object — this is the pattern in action, not just theory.

### 57:17 — Explain the difference between @classmethod and instance methods.

- **Short answer:** Instance methods take `self` and operate on one specific object's data; you need an instance to call them. Class methods take `cls` instead of `self`, operate on the class itself (not a specific instance), and can be called directly on the class without creating an object first. (A related third option, `@staticmethod`, takes neither `self` nor `cls` — it's just a regular function grouped inside the class for organization.)
- **Code:**
```python
class MyClass:
    @classmethod
    def class_method(cls):
        return "Class method called"

    def instance_method(self):
        return "Instance method called"

obj = MyClass()
print(MyClass.class_method())   # works without creating an instance
print(obj.instance_method())    # needs an instance
```
- **Connection to my repo:** N/A — your page classes use regular instance methods since each one needs `self.driver`.

---

## Block 3 — Pytest specific

### 17:54 — What are fixtures in Pytest? When are they used?

- **Short answer:** Fixtures are functions decorated with `@pytest.fixture` that set up something a test needs (data, a browser session, a database connection) before the test runs, and can clean it up afterward. They're passed into test functions as arguments, and pytest handles calling them automatically.

  Key features:
  1. Reusability — define once, use across many tests
  2. Automatic setup and teardown
  3. Scope control — fixtures can run per test, per class, per module, or per session
  4. Dependency injection — tests just declare the fixture as a parameter
- **Code:**
```python
import pytest

@pytest.fixture
def sample_data():
    print("\nSetup: Creating test data")
    data = {"name": "Alice", "age": 30}
    return data

def test_example(sample_data):
    assert sample_data["name"] == "Alice"
```
- **Connection to my repo:** Your `conftest.py` fixture that instantiates the WebDriver (with the `--browser_name` flag choosing Chrome or Firefox) is exactly this pattern — every test that needs a browser just declares the fixture as a parameter.

### 22:02 — How do you use yield for WebDriver setup and teardown in pytest?

- **Short answer:** Using `yield` instead of `return` in a fixture lets you split it into two parts: everything before `yield` runs as setup (before the test), and everything after `yield` runs as teardown (after the test finishes, even if it failed). For WebDriver, that means launching the browser before `yield` and calling `driver.quit()` after it.
- **Code:**
```python
import pytest

@pytest.fixture
def sample_data():
    print("\nSetup: Creating test data")
    data = {"name": "Alice", "age": 30}
    yield data
    print("\nTeardown: Cleaning up test data")

def test_example(sample_data):
    assert sample_data["name"] == "Alice"
```
- **Connection to my repo:** This is exactly what your `conftest.py` driver fixture does — it sets up the WebDriver (with Chrome/Firefox flags like `--no-sandbox`, `--disable-dev-shm-usage`, and `--headless=new` for Jenkins) before `yield`, and calls `driver.quit()` after, guaranteeing the browser closes even if the test fails.

### 01:01:15 — What is the use of the conftest.py file in Python pytest?

- **Short answer:** `conftest.py` is a special pytest file where you define fixtures, hooks, and command-line options that are automatically shared across every test file in that directory (and subdirectories) — without needing to import anything.
- **Code:**
```python
# conftest.py
import pytest

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture
def browser_name(request):
    return request.config.getoption("--browser_name")
```
- **Connection to my repo:** This is a direct match — your `conftest.py` registers the `--browser_name` command-line flag (Chrome/Firefox) and defines the WebDriver fixture that every test in the suite uses, including in your Jenkins pipeline command (`--browser_name "$browser"`).

### 01:03:51 — How do you execute only failed test cases in pytest?

- **Short answer:** Run `pytest --lf` (or `--last-failed`) to re-run only the tests that failed in the previous run. There's also `--ff`/`--failed-first`, which runs the previously failed tests first and then the rest.
- **Code:**
```bash
python3 -m pytest --lf
```
- **Connection to my repo:** N/A — haven't used `--lf` in your workflow yet, but it's directly usable with your existing `python3 -m pytest` setup since it's a built-in flag, no extra configuration needed.

### 01:04:55 — How do you apply a custom marker to a test case in pytest?

- **Short answer:** Decorate a test with `@pytest.mark.<name>`, then run only tests with that marker using `pytest -m <name>`. Custom markers should be registered (in `pytest.ini` or `conftest.py`) to avoid pytest warnings about unknown markers.
- **Code:**
```python
import pytest

@pytest.mark.sanity
def test_example():
    assert True
```
```bash
pytest -m sanity
```
- **Connection to my repo:** This is exactly what your `smoke` marker does — tests are decorated with `@pytest.mark.smoke`, and your Jenkins pipeline runs only those with `python3 -m pytest -m smoke --browser_name "$browser" --html=reports/report.html`.

---

## General notes / open questions
-
