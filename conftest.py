import pytest
from Config.config import TestData

from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--env", action="store", default="dev")

@pytest.fixture()
def init_driver(request , pytestconfig):
    browser_name = pytestconfig.getoption("browser")
    web_driver = None
    if browser_name == "chrome":
        web_driver = webdriver.Chrome()


    if browser_name == "firefox":
        web_driver = webdriver.Firefox()
        request.cls.driver = web_driver
    # init_driver = web_driver

    yield web_driver
    web_driver.close()

@pytest.fixture()
def env(pytestconfig):
    return pytestconfig.getoption("env")

@pytest.fixture()
def app_url(env):

    if env == "qa":
        return TestData.BASE_URL_QA
    else:
        return TestData.BASE_URL_DEV

