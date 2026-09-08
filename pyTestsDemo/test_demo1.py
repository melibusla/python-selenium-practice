#Naming conventions: tests should start or end with 'test_'/'_test'
#Write everything in functions and start with 'test_'
#Pytests can either run by the IDE or the terminal, from the package and py.test
    # to see more info: python3 -m pytest -v
        #-v verbose, more info
    # to see the logs: python3 -m pytest -v -s
    #To run a specific file: python -m pytest file.py -v -s
    #In linux ubuntu: python3 -m pytest test_demo2.py -v -s
    #To run some related test cases from 2 files: python3 -m pytest -k CreditCard -v -s
        #-k regular expression
    #Mark: similar to tags, import and create tag with '@pytest.mark.[name]'
        #Run with: python3 -m pytest -m smoke -v -s
        #-m mark
    #Ignore a case with a predefined mark: '@pytest.mark.skip'
    #To run but not report it: '@pytest.mark.xfail'
    #Fixture: methods ran first, opening a browser, env variables: '@pytest.fixture()'
        #yield will run after the first code is executed
        #add it in a separate file called 'conftest' if it will be shared across multiple tests
        #If the standard is in many test cases within a file, wrap them in a class and apply it the '@pytest.mark.usefixtures("setup)
            # to apply it at class level (runs once at the beginning not for each test), add 'scope="class"' to the conftest method
    #Datadriven and parameterization can be done with return statements in tuple format
    #Save to a html file: pytest --html=report.html => python3 -m pytest --html=report.html -v -s

import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    print("Hello World")

def test_secondGreetCreditCard():
    print("Bye")

def test_crossBrowser(crossBrowser):
    print(crossBrowser)

# def test_crossBrowser2(crossBrowser2):
#     print(crossBrowser2[1])