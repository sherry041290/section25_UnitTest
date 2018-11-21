import pytest


@pytest.fixture()
def setUp():
    print("--Before test: ")
    yield
    print("--After test! ")


@pytest.fixture(scope="class")
def oneTimeSetUp(browser, ostype):
    print("--Running once time setUp")
    if browser == 'firefox':
        print("Run test on Firefox")
    else:
        print(" Run test on Chrome")
    yield
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

