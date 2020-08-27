# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "5.1.1"
caps["deviceName"] = "127.0.0.1:62001"
caps["app"] = "C:\\Users\\Administrator\\Desktop\\App\\yidongzixishi_4.6.1.apk"
caps["appPackage"] = "com.offcn.yidongzixishi"
caps["appActivity"] = "com.offcn.yidongzixishi.SplashActivity"
caps["noReset"] = False

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
time.sleep(3)
driver.find_element_by_id("com.offcn.yidongzixishi:id/skip").click()
driver.find_element_by_id("com.offcn.yidongzixishi:id/et_phone").send_keys("13242849900")
driver.find_element_by_id("com.offcn.yidongzixishi:id/et_pwd").click()
driver.find_element_by_id("com.offcn.yidongzixishi:id/et_pwd").send_keys("13242849900qjx~")
driver.find_element_by_id("com.offcn.yidongzixishi:id/btn_login").click()
time.sleep(3)
q=TouchAction(driver)
q.press(x=521, y=1155)
q.move_to(x=61, y=-768)
q.release()
q.perform()
time.sleep(3)
driver.find_element_by_xpath("/hierarchy"
                             "/android.widget.FrameLayout"
                             "/android.widget.LinearLayout"
                             "/android.widget.FrameLayout"
                             "/android.widget.LinearLayout"
                             "/android.widget.FrameLayout"
                             "/android.widget.LinearLayout"
                             "/android.widget.LinearLayout"
                             "/android.widget.RelativeLayout"
                             "/android.support.v7.widget.RecyclerView"
                             "/android.widget.LinearLayout[4]"
                             "/android.widget.RelativeLayout"
                             "/android.widget.TextView").click()
time.sleep(5)
driver.find_element_by_id("com.offcn.yidongzixishi:id/cancel").click()
driver.find_element_by_id("com.offcn.yidongzixishi:id/rl_mine").click()
driver.find_element_by_id("com.offcn.yidongzixishi:id/iv_user").click()
driver.find_element_by_xpath("/hierarchy"
                             "/android.widget.FrameLayout"
                             "/android.widget.LinearLayout"
                             "/android.widget.FrameLayout"
                             "/android.widget.LinearLayout"
                             "/android.widget.FrameLayout"
                             "/android.widget.LinearLayout"
                             "/android.widget.RelativeLayout[2]").click()
driver.find_element_by_id("com.offcn.yidongzixishi:id/userPhoto").click()
driver.find_element_by_id("com.offcn.yidongzixishi:id/wifiToggle").click()
time.sleep(3)
driver.quit()