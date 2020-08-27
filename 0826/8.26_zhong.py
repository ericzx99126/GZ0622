'''
1.课上知识和代码复习。
2.Appium脚本实现考研帮用户注册：
进入注册界面设置头像，填写信息并完成注册。要求，重复执行时用户名不能重复。注册成功后截图保存并退出账号。（参考selenium截图方法）
3.Appium中常用的定位方式有哪些？不常用的不用写。
4.Git有哪些基本命令，作用分别是什么？
5.Git的三个工作区分别是什么？
'''
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
caps = {


}
caps["platformName"] = "Android"
caps["platformVersion"] = "5.1.1"
caps["deviceName"] = "127.0.0.1:62001"
caps["app"] = "C:\\Users\\Administrator\\Desktop\\App\\kaoyan3.1.0.apk"
caps["appPackage"] = "com.tal.kaoyan"
caps["appActivity"] = "com.tal.kaoyan.ui.activity.SplashActivity"
caps["noReset"] = False
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
TouchAction(driver)
el1 = driver.find_element_by_id("android:id/button2")
el1.click()
driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()
driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
time.sleep(2)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys('aJURfafY')
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys('abcd6606')
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys('21788933@qq.com')
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()
time.sleep(3)
driver.save_screenshot('./pic/注册成功.png')
driver.find_element_by_id('com.tal.kaoyan:id/perfectinfomation_edit_school_name').click()
driver.find_element_by_id('com.tal.kaoyan:id/more_forum_title').click()
driver.find_element_by_id('com.tal.kaoyan:id/university_search_item_name').click()
driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_major').click()
driver.find_element_by_id('com.tal.kaoyan:id/major_subject_title').click()
driver.find_element_by_id('com.tal.kaoyan:id/major_search_item_name').click()
driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_goBtn').click()
driver.find_element_by_id("com.tal.kaoyan:id/view_wemedia_cacel").click()
driver.find_element_by_id("com.tal.kaoyan:id/task_no_task").click()
driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_RightButton_textview').click()
driver.find_element_by_id('com.tal.kaoyan:id/setting_logout_text').click()
driver.get_screenshot_as_file('./pic/退出登录.png')
driver.find_element_by_id('com.tal.kaoyan:id/tip_commit').click()











