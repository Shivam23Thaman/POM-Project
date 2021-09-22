# import sys
# sys.path.append("/home/shivam/Documents/selenium_novice_project")
from utilities.teststatus import TestStatus
from base.basepage import BasePage
from pages.courses.register_courses_page1 import RegisterCoursesPage
import time
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCourseTests(unittest.TestCase, BasePage):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.rc = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        search_results = self.rc.enterCourseName('Java')
        time.sleep(2)
        self.rc.open_course("JavaScript for beginners")
        self.rc.click_enroll_button()
        self.rc.buyCourse(num="1234 5678 9012 3456", exp="1220", cvv="444")
        result1 = self.rc.verify_order_contact_payment_block_exists()
        self.ts.mark(result1, "Any of the necessary blocks do not exist")
        result2 = self.rc.verifyErrorMsgDisp()
        self.ts.mark(result2, "Error Message not Displayed")
        result3 = self.rc.verifyBuyButtonDisabledOnError()
        self.ts.markFinal("test_invalidEnrollment", result3, "Course Enrollemnt Failed")

    @pytest.mark.run(order=2)
    def test_logout_contact_info(self):
        self.webScroll(direction='up', px=1000)
        self.rc.logout_contact_info_link()
        result = self.rc.verify_logout()
        self.ts.markFinal('test_logout_contact_info', result, 'logout from contact info failed.')

    @pytest.mark.run(order=3)
    def test_buying_while_logout(self): # logged out but trying to buy the course
        time.sleep(3)
        self.webScroll(direction='down', px=800)
        self.rc.clearCardFields()
        self.rc.buyCourse('411111111111', '1231', '134')
        result1 = self.rc.verifyErrorMsgDisp()
        self.ts.mark(result1, "Error Message not Displayed")
        result2 = self.rc.verifyBuyButtonDisabledOnError()
        self.ts.markFinal("test_buying_after_logout", result2, "Was able to buy while logged out")

     


