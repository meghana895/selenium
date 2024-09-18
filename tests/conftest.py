import pytest
from selenium import webdriver
from config import Config


@pytest.fixture
def driver_init():
    browser=Config.browser
    if browser.lower() =="chrome":
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=opts)

    elif browser.lower() =="firefox":
        driver=webdriver.Firefox()

    else:
        driver=webdriver.Edge()

    driver.get(Config.url)
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.close()







