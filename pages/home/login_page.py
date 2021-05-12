import sys 
sys.path.append("/home/shivam/Documents/selenium_novice_project")
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "a[href='/login']"
    _email_field = "input[placeholder='Email Address']"
    _password_field = "password"
    _login_button = "//input[@value='Login']"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="css")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="css")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        try:
            self.clickLoginLink()
            self.enterEmail(email)
            self.enterPassword(password)
            self.clickLoginButton()
        except:
            print("Some Eception Occured")

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//button[@id='dropdownMenu1']/img",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[@class='form-group has-error']//span[contains(text(), 'username or password is invalid')]",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("All Courses")