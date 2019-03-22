from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy

# create dictionary for desire capability
desired_cap = {
    'platformName': 'Android',
    'deviceName': 'Android Emulator',
    'appPackage': 'com.walmart.android',
    'appWaitActivity': 'com.walmart.android.app.main.HomeActivity',
    'app': 'C:\\Users\\airlay\\Downloads\\Appium\\Walmart_v19.8_apkpure.com.apk'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

driver.implicitly_wait(30)

# homebar = driver.find_elements_by_class_name('android.widget.Button')
#
# print(homebar)
#
# for i in homebar:
#     print(i.text)




# TouchAction(driver).press(x=361, y=1135).move_to(x=433, y=1139).release().perform()
# TouchAction(driver).press(x=433, y=1189).move_to(x=689, y=1172).release().perform()
# driver.implicitly_wait(30)
#
# el1 = driver.find_element_by_accessibility_id("The Spring Shop. Fresh finds in fashion, travel & home.")
# el1.click()
# driver.implicitly_wait(30)
#
# el2 = driver.find_element_by_xpath(
#     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.RelativeLayout[3]/android.widget.TextView")
# el2.click()


el3 = driver.find_element_by_accessibility_id('Open navigation drawer')

el3.click()

# els = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView")


# els = driver.find_element_by_id('com.walmart.android:id/design_navigation_view')
#
# print('here here')
# print(els.size)
# print('here')
#
els1 = driver.find_elements_by_class_name('android.widget.CheckedTextView')
for i in els1:
    print(i.text)
driver.find_element_by_id


#
#
# els1[1].click()

# driver.find_element_by_id('com.walmart.android:id/design_menu_item_text')

# com.walmart.android:id/design_navigation_view


# go back to home
# driver.keyevent(3)
