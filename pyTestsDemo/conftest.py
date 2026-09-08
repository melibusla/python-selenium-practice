import pytest

# @pytest.fixture()
# def setup():
#     print("I'll be executed first")
#     yield
#     print("I'll be executed last")

@pytest.fixture(scope="class") #runs only once at class level
def setup():
    print("I'll be executed first")
    yield
    print("I'll be executed last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Mel", "B" , "test@test.com"]

@pytest.fixture(params=["chrome", "firefox", "safari"])
def crossBrowser(request):
    return request.param

# @pytest.fixture(params=[("chrome", "Melina", "Bu"), ("firefox", "Fulano", "V"), "safari"])
# def crossBrowser2(request):
#     return request.param