import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver_init(request):

    driver = None

    if request.param == "chrome":
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
    if request.param == "firefox":
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX)
    if request.param == "edge":
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.EDGE)

    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.usefixtures("driver_init")
class BasicChromeTest:
    pass


class TestURLChrome(BasicChromeTest):
    @pytest.mark.parametrize("url", ["https://www.google.com"])
    def test_first_case(self, url):
        self.driver.get(url)
        assert "Google" == self.driver.title
        time.sleep(2)
