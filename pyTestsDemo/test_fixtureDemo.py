import pytest

# @pytest.fixture()
# def setup():
#     print("I'll be executed first")
#     yield
#     print("I'll be executed last")

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("I'll execute steps in fixtureDemo")

    def test_fixtureDemo2(self):
        print("I'll execute steps in fixtureDemo2")

    def test_fixtureDemo3(self):
        print("I'll execute steps in fixtureDemo3")

    def test_fixtureDemo4(self):
        print("I'll execute steps in fixtureDemo4")