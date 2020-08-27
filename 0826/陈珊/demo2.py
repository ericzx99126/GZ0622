from appium import webdriver
import time

caps= {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "127.0.0.1:62001",
  "app": "C:\\Users\\Administrator\\Desktop\\App\\kaoyan3.1.0.apk",
  "appPackage": "com.tal.kaoyan",
  "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
  "noReset": False
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)


el1 = driver.find_element_by_id("android:id/button2")
el1.click()
el2 = driver.find_element_by_id("com.tal.kaoyan:id/tv_skip")
el2.click()
el3 = driver.find_element_by_id("com.tal.kaoyan:id/login_register_text")
el3.click()
el4 = driver.find_element_by_id("com.tal.kaoyan:id/activity_register_username_edittext")
el4.send_keys("xiayule150")
el5 = driver.find_element_by_id("com.tal.kaoyan:id/activity_register_password_edittext")
el5.send_keys("xiayu123456")
el6 = driver.find_element_by_id("com.tal.kaoyan:id/activity_register_email_edittext")
el6.send_keys("284759321@qq.com")
el7 = driver.find_element_by_id("com.tal.kaoyan:id/activity_register_register_btn")
el7.click()

el11 = driver.find_element_by_id("com.tal.kaoyan:id/perfectinfomation_edit_school_name")
el11.click()
el12 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.LinearLayout[8]/android.widget.TextView[1]")
el12.click()
el13 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.LinearLayout[10]")
el13.click()
el14 = driver.find_element_by_id("com.tal.kaoyan:id/activity_perfectinfomation_major")
el14.click()
el15 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[4]/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.TextView")
el15.click()
el16 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.LinearLayout[11]/android.widget.TextView")
el16.click()
el17 = driver.find_element_by_id("com.tal.kaoyan:id/activity_perfectinfomation_goBtn")
el17.click()
el18 = driver.find_element_by_id("com.tal.kaoyan:id/view_wemedia_cacel")
el18.click()
el19 = driver.find_element_by_id("com.tal.kaoyan:id/task_no_task")
el19.click()


el21 = driver.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl")
el21.click()
time.sleep(3)
driver.save_screenshot('个人页面.png')
el22 = driver.find_element_by_id("com.tal.kaoyan:id/myapptitle_RightButtonWraper")
el22.click()
el23 = driver.find_element_by_id("com.tal.kaoyan:id/setting_logout_text")
el23.click()
el24 = driver.find_element_by_id("com.tal.kaoyan:id/tip_commit")
el24.click()
time.sleep(2)
driver.save_screenshot('退出成功.png')