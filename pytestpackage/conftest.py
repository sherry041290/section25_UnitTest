import pytest


@pytest.fixture()
def setUp():
    print("--Before test: ")
    yield
    print("--After test! ")


@pytest.fixture(scope="class")
def oneTimeSetUp(browser, request):
    print("--Running once time setUp")
    if browser == 'firefox':
        value = 10
        print("Run test on Firefox")
    else:
        value = 20
        print(" Run test on Chrome")
    if request.cls is not None:
        request.cls.value = value
    yield value
    print("--Running once time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser", help="enter browser")
    parser.addoption("--ostype", help="type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def ostype(request):
    return request.config.getoption("--ostype")

