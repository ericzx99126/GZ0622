from appium import webdriver
import time
import random

caps={
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "127.0.0.1:62001",
  "app": "E:\\App\\kaoyan3.1.0.apk",
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
time.sleep(2)

#点击图像保存
driver.find_element_by_id('com.tal.kaoyan:id/save').click()

#输入用户名
driver.find_element_by_class_name('android.widget.EditText').send_keys('hxmimg1215')

#输入密码
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys('huxiaoming1215')
#输入email
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys('hxm1215@qq.com')
#点击立即注册
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()
time.sleep(3)
#截图
now_time=time.strftime('%Y%m%d_%H%M%S')
driver.get_screenshot_as_file('img%s.png'%now_time)
#点击设置
driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_RightButton_textview').click()
#点击退出登录
driver.find_element_by_id('com.tal.kaoyan:id/setting_logout_text').click()
#点击确认按钮
driver.find_element_by_id('com.tal.kaoyan:id/tip_commit').click()



time.sleep(2)
driver.quit()
