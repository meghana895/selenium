from logging import exception

import pytest
from src.registration_page import RegistrationPage
from utilities.selenium_wrapper import capture_screenshot


data=[("tom","cruise","tomcruise123@gmail.com","tom123","tom123")]

@pytest.mark.parametrize("firstname,lastname,email,pwd,confirmpwd",data)
def test_register(driver_init,firstname,lastname,email,pwd,confirmpwd):
    driver=driver_init
    try:
        rp=RegistrationPage(driver)
        rp.register(firstname,lastname,email,pwd,confirmpwd)
        exists = rp.is_user_already_exists()
        assert exists, "user already exists"

    except Exception as error:
        capture_screenshot(driver,"test_register")
        print(f"testcase failed due to {error}")
        raise error


