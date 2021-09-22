import unittest
from tests.home.login_tests import LoginTests
from tests.courses.register_courses_tests1 import RegisterCourseTests

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCourseTests)

smokeTests = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTests)