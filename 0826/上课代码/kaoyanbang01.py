# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
#
# 导包
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

# 配置信息：
# 客户端要首先发给服务器的信息，指明设备类型、设备ID、操作系统版本、应用包名、应用启动Activity名称、是否以重置状态启动
caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "5.1.1"
caps["deviceName"] = "127.0.0.1:62001"
caps["app"] = "D:\\apk\\kaoyan3.1.0.apk"
caps["appPackage"] = "com.tal.kaoyan"
caps["appActivity"] = "com.tal.kaoyan.ui.activity.SplashActivity"
caps["noReset"] = False

# caps = {
#   "platformName": "Android",
#   "platformVersion": "5.1.1",
#   "deviceName": "127.0.0.1:62001",
#   "app": "D:\\apk\\kaoyan3.1.0.apk",
#   "appPackage": "com.tal.kaoyan",
#   "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
#   "noReset": False
# }

# 创建远程设备对象，配置信息作为第二个参数
# 第一个参数为Appium服务器的地址
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

# 元素定位与操作
driver.find_element_by_id("android:id/button2").click()
driver.find_element_by_id("com.tal.kaoyan:id/tv_skip").click()
driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").send_keys("zgjy1234")
driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("zgjy123456")
TouchAction(driver).tap(x=445, y=624).perform()
driver.find_element_by_id("com.tal.kaoyan:id/view_wemedia_cacel").click()
driver.find_element_by_xpath("/hierarchy"
                             "/android.widget.FrameLayout"
                             "/android.widget.LinearLayout"
                             "/android.widget.FrameLayout"
                             "/android.widget.LinearLayout"
                             "/android.widget.FrameLayout"
                             "/android.support.v4.view.ViewPager"
                             "/android.widget.FrameLayout"
                             "/android.widget.LinearLayout[2]"
                             "/android.widget.ListView"
                             "/android.widget.LinearLayout"
                             "/android.widget.RelativeLayout"
                             "/android.widget.RelativeLayout").click()
driver.find_element_by_xpath("/hierarchy"
                             "/android.widget.FrameLayout"
                             "/android.widget.LinearLayout"
                             "/android.widget.FrameLayout"
                             "/android.widget.LinearLayout"
                             "/android.widget.FrameLayout"
                             "/android.support.v4.view.ViewPager"
                             "/android.widget.FrameLayout"
                             "/android.widget.LinearLayout[1]"
                             "/android.widget.ListView"
                             "/android.widget.LinearLayout"
                             "/android.widget.RelativeLayout"
                             "/android.widget.RelativeLayout").click()


driver.quit()

