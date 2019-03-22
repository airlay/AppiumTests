import unittest
# from appium.webdriver.common.mobileby import MobileBy
from Driver import Driver
from appium.webdriver.common.touch_action import TouchAction


class WalmartTestCases(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()

    def test_walmart_lunches(self):
        self.driver.instance.implicitly_wait(30)
        TouchAction(self.driver.instance).press(x=361, y=1135).move_to(x=433, y=1139).release().perform()
        self.driver.instance.implicitly_wait(30)
        self.driver.instance.find_element_by_accessibility_id("Browse Electronics.").click()

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WalmartTestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)
