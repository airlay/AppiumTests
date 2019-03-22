from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WalmartMainScreen:

    # class vaeriable
    allhomebuttoms = ['Furniture', 'Health', 'Beauty', 'Jewelry', 'Pickup Today', 'Home Improvement', 'Home', 'Clothing',
                      'All', 'Savings Center', 'Easter', 'Electronics', 'Patio & Garden', 'Toys', 'Food',
                      'Household Essentials', 'Baby & Toddler', 'Personal Care']

    def __init__(self, driver):
        # check if some of the bottoms shows up after initiating driver instance
        self.driver = driver
        self.navigation = WebDriverWait(self.driver.instance, 60).until(
            EC.visibility_of_element_located((MobileBy.ID, "Open navigation drawer")))
        self.all = WebDriverWait(self.driver.instance, 60).until(
            EC.visibility_of_element_located((MobileBy.ID, "Browse all departments.")))
        self.savingcenter = WebDriverWait(self.driver.instance, 60).until(
            EC.visibility_of_element_located((MobileBy.ID, "Browse Savings Center.")))
        self.electronic = WebDriverWait(self.driver.instance, 60).until(
            EC.visibility_of_element_located((MobileBy.ID, "Browse Electronics.")))



    def test(self):

        assert 1 ==1

    def navigationtest(self):

        # check whether one of the buttom on navigation shows up
        nevbottom  = self.driver.instance.find_element_by_accessibility_id('Open navigation drawer')
        nevbottom.click()
        els = self.driver.instance.find_elements_by_class_name('android.widget.CheckedTextView')
        l = []
        for i in els:
            # print(i.text)
            l.append(i.text)
        assert 'Shop by Department' in l


    def mainpagetest(self):
        # check if any of the home buttoms presents after logging in.
        # the get elements result is check against the list in the class
        homebuttoms = self.driver.instance.find_elements_by_class_name('android.widget.Button')
        m = []
        for i in homebuttoms:
            print('what do we have in homebuttoms : {}'.format(i.text))
            if i.text in self.allhomebuttoms:
                m.append(i.text)


        assert len(m) > 0


    def mainpagesearchtest(self):
        searchbuttom = self.driver.instance.find_element_by_id('com.walmart.android:id/search_src_text')
        assert searchbuttom.text == 'Search stores & online'
        searchbuttom.click()



