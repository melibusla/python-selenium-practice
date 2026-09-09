# Python Selenium Practice

Web automation exercises and practice with **Python + Selenium**, done as part of the [Learn Selenium Automation in Easy Python Language](https://www.udemy.com/course/learn-selenium-automation-in-easy-python-language/) Udemy course.

This repo serves as a learning log: from Python fundamentals to Selenium WebDriver handling (locators, element interactions, forms, etc.), on the path from manual QA to automation QA.

## 📁 Repository structure

```
python-selenium-practice/
├── PythonBasics/     # Python fundamentals (data types, loops, functions, OOP, exceptions, file I/O)
│                     # + cheat-sheet-string-extraction-python.md
├── SeleniumBasics/   # Standalone Selenium scripts by topic: locators, waits, alerts, iframes,
│                     # actions, JavaScript executor, file upload, Chrome options
│                     # + cheat-sheet-locators-selenium.md and selenium_notes.md
├── pyTestsDemo/      # pytest fundamentals: fixtures, markers, parametrization
├── e2ePractice/      # Small POM-based test framework: page objects, data-driven tests (JSON),
│                     # Chrome/Firefox support, pytest-html reports with screenshot-on-failure
├── resources/        # Raw course materials
└── .gitignore
```

> Note: as the course progresses, this structure and the details of each folder will keep getting updated.

## 🛠️ Tech stack

- **Python 3.10**
- **Selenium 4.x** — using Selenium Manager, so no manual ChromeDriver setup or `Service` object is needed
- **pytest**, with `pytest-html` for HTML reports in `pyTestsDemo/` and `e2ePractice/`
- Developed on **Ubuntu Linux** with **PyCharm**

## ▶️ How to run the exercises

1. Clone the repository:
   ```bash
   git clone https://github.com/melibusla/python-selenium-practice.git
   cd python-selenium-practice
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install selenium pytest pytest-html
   ```
4. Run a standalone script (`PythonBasics/`, `SeleniumBasics/`):
   ```bash
   python3 SeleniumBasics/script_name.py
   ```
5. Run a pytest suite (`pyTestsDemo/`, `e2ePractice/`):
   ```bash
   python3 -m pytest pyTestsDemo -v -s
   python3 -m pytest e2ePractice -v -s
   ```
   `e2ePractice` also supports choosing the browser:
   ```bash
   python3 -m pytest e2ePractice --browser_name firefox -v -s
   ```

> Note: exercises here are developed and run on Ubuntu, so commands use `python3`. If you're on Windows/macOS, use `python` instead where relevant.

## 🎯 Goal

This repo is part of my transition from manual QA to automation QA, documenting practice from the Udemy course and serving as a future reference for Selenium syntax and patterns in Python.

## 📌 Status

🚧 In progress — currently covering locator strategies, waits, child/browser windows, iframes, and a small Page Object Model framework with data-driven tests and HTML reporting (`e2ePractice/`). Updated as I move forward with the course.
