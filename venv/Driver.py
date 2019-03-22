from appium import webdriver

class Driver:

    def __init__(self):
        desired_cap = {
            'platformName': 'Android',
            'deviceName': 'Android Emulator',
            'appPackage': 'com.walmart.android',
            'appWaitActivity': 'com.walmart.android.app.main.HomeActivity',
            'app': 'C:\\Users\\airlay\\Downloads\\Appium\\Walmart_v19.8_apkpure.com.apk'
        }

        self.instance = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

        