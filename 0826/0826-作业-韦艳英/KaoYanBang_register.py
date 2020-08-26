from appium import webdriver
from time import sleep
import random
from selenium import webdriver
import time

caps = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "127.0.0.1:62025",
  " app": "C:\\Users\\Administrator\\Desktop\\kaoyan3.1.0.apk",
  "appPackage": "com.tal.kaoyan",
  "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
  "noReset":True
}

dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)

sleep(10)
# 点击 “我”
dr.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
sleep(1)
# 点击 头像
dr.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_userheader').click()
sleep(2)
# 注册
dr.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
sleep(2)
# 添加头像
dr.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()
sleep(2)
# list定位（find_elements方法）
pics =dr.find_elements_by_xpath('//android.widget.GridView//android.widget.ImageView')
print(len(pics))
random.choice(pics[1:]).click()
sleep(1)
# 点击 保存  头像
dr.find_element_by_id('com.tal.kaoyan:id/save').click()
sleep(1)
# 用户名
dr.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys('wyyq6666')
sleep(1)
# 密码
dr.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys('yy123123')
sleep(1)
# Email
dr.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys('187777@126.com')
sleep(2)
# 我已阅读并遵守  考研网服务条款
# dr.find_element_by_id('com.tal.kaoyan:id/activity_register_article_checkbox').click()
# sleep(1)
# 立即注册
dr.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()
sleep(2)
# 截图
# dr.save_screenshot('./img/img01.png')

now_time = time.strftime('%Y_%m_%d %H_%M_%S')
# 截图，保存
dr.get_screenshot_as_file('./img_%s.png' % now_time)

# 退出登录   设置按钮
dr.find_element_by_id('com.tal.kaoyan:id/myapptitle_RightButton_textview').click()
sleep(1)
# 退出登录
dr.find_element_by_id('com.tal.kaoyan:id/setting_logout_text').click()
sleep(1)
# 确定按钮
dr.find_element_by_id('com.tal.kaoyan:id/tip_commit').click()

sleep(5)
dr.quit()
































































