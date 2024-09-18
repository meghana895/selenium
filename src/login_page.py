# class LoginPage:
#     login_link=("link text","Log in")
#     email_text=("id","Email")
#     pwd_text=("id","Password")
#     rememberme_btn=("id","RememberMe")
#     login_text_link=("xpath",'//input[@value="Log in"]')
#
#     def __init__(self,driver):
#         self.driver=driver
#
#     def login(self,email,password):
#         self.driver.find_elementlement(*self.login_link).click()
#         self.driver.find_element(*self.email_text).send_keys(email)
#         self.driver.find_element(*self.pwd_text).send_keys(password)
#         self.driver.find_element(*self.rememberme_btn).click()
#
#     def is_user_logged_in(self):
