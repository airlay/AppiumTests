import unittest
from walmart_main_screen import WalmartMainScreen
from Driver import Driver



class WalmartMainScreenTestCases(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()

    def test_main_screen_lunch(self):
        walmart = WalmartMainScreen(self.driver)
        # walmart.test()
        walmart.navigationtest()
        walmart.mainpagetest()



    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WalmartMainScreenTestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)

