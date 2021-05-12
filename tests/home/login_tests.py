import sys 
sys.path.append("/home/shivam/Documents/selenium_novice_project")
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title Verification")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login Verification")

    
    @pytest.mark.xfail
    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        try:
            self.lp.login("test@email.com", "abcabcabc")
            result = self.lp.verifyLoginFailed()
        except:
            print("Could not fill the values.")
        assert result == True
        #self.ts.markFinal("test_invalidLogin", result, "Login Verification")