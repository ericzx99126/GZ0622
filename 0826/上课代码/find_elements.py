from appium import webdriver
import time,random

caps= {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "127.0.0.1:62001",
  "app": "D:\\apk\\kaoyan3.1.0.apk",
  "appPackage": "com.tal.kaoyan",
  "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
  "noReset": True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)

time.sleep(5)

# 我
driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()

# 头像
driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_userheader').click()

# 注册
driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()

# 头像
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()

# List定位（find_elements方法）
pics=driver.find_elements_by_xpath('//android.widget.GridView//android.widget.ImageView')
print(len(pics))
random.choice(pics[1:]).click()

time.sleep(6)

#
driver.quit()
