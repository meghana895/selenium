from selenium.common.exceptions import NoSuchElementException
from config import Config


class RegistrationPage():
    reg_link=("link text","Register")
    gender_male_btn=("id","gender-male")
    gender_female_btn=("id","gender-female")
    first_name_text=("id","FirstName")
    last_name_text=("id","LastName")
    email_text=("id","Email")
    pwd_text=("id","Password")
    confirm_pwd_text=("id","ConfirmPassword")
    register_btn=("id","register-button")
    register_text=("xpath",'//li[text()="The specified email already exists"]')


    def __init__(self,driver):
        self.driver=driver

    # def register(self):
        # self.driver.find_element(*self.reg_link).click()
        # self.driver.find_element(*self.gender_male_btn).click()
        # # self.driver.find_element(*self.gender_female_btn).click()
        # self.driver.find_element(*self.first_name_text).send_keys("tom")
        # self.driver.find_element(*self.last_name_text).send_keys("cruise")
        # self.driver.find_element(*self.email_text).send_keys("tomcruise123@gmail.com")
        # self.driver.find_element(*self.pwd_text).send_keys("tom123")
        # self.driver.find_element(*self.confirm_pwd_text).send_keys("tom123")
        # self.driver.find_element(*self.register_btn).click()
        # time.sleep(2)
    def register(self,firstname,lastname,email,pwd,confirmpwd):

        self.driver.find_element(*self.reg_link).click()
        self.driver.find_element(*self.gender_male_btn).click()
        # self.driver.find_element(*self.gender_female_btn).click()
        self.driver.find_element(*self.first_name_text).send_keys(firstname)
        self.driver.find_element(*self.last_name_text).send_keys(lastname)
        self.driver.find_element(*self.email_text).send_keys(email)
        self.driver.find_element(*self.pwd_text).send_keys(pwd)
        self.driver.find_element(*self.confirm_pwd_text).send_keys(confirmpwd)
        self.driver.find_element(*self.register_btn).click()

    def is_user_already_exists(self):
        try:
            self.driver.find_element(*self.register_text)
            return False

        except NoSuchElementException:
            return True






