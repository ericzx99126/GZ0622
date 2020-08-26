from appium import webdriver
import time

caps= {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "127.0.0.1:62001",
  "app": "D:\\apk\\kaoyan3.1.0.apk",
  "appPackage": "com.tal.kaoyan",
  "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
  "noReset": False
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)

# by_id
# 点击取消更新
driver.find_element_by_id('android:id/button2').click()
# 点击跳过引导页
driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()

# by_name
# driver.find_element_by_name('跳过 > ').click()

# by_class_name
# 点击跳过按钮
driver.find_element_by_class_name('android.widget.ImageView').click()
# 输入用户名
driver.find_element_by_class_name('android.widget.EditText').send_keys('zgjy1234')
# 输入密码
driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('zgjy123456')

# 相对定位
# 先找到登录按钮的上上级元素
grand_father = driver.find_element_by_id('com.tal.kaoyan:id/login_parent_layout')
father = grand_father.find_element_by_class_name('android.widget.LinearLayout')
login_button = father.find_element_by_class_name('android.widget.Button')
login_button.click()

# xpath定位
time.sleep(2)

# 绝对路径
# 点击广告右上角的x
# driver.find_element_by_xpath('/hierarchy'
#                              '/android.widget.FrameLayout'
#                              '/android.widget.LinearLayout'
#                              '/android.widget.FrameLayout'
#                              '/android.widget.RelativeLayout'
#                              '/android.widget.RelativeLayout'
#                              '/android.widget.ImageView[2]').click()

# 相对路径
# 点击广告右上角的x
time.sleep(3)

# 有问题
driver.find_element_by_xpath('//android.widget.ImageView[@resourse-id="com.tal.kaoyan:id/view_wemedia_image"]'
                             '/../android.widget.ImageView[2]').click()

# 点击“我知道了”
# time.sleep(2)
# driver.find_element_by_xpath('//android.widget.RelativeLayout[@resource-id="com.tal.kaoyan:id/date_task_layout"]'
#                              '/android.widget.RelativeLayout').click()

time.sleep(3)

#
driver.quit()
