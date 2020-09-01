"""
Page created by Jinal Shah
Wrote test case for checking laptop value

"""

from appium import webdriver
import time
import os
import base64
from appium.webdriver.common.touch_action import TouchAction

# capabilities
desired_cap = {
    "deviceName": "29d5d20a0104",
    "platformName": "Android",
    "appPackage": "com.flipkart.android",
    "appActivity": "com.flipkart.android.activity.HomeFragmentHolderActivity",
    "automationName": "UiAutomator2"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(10)

# Start recording
driver.start_recording_screen()
# Go to Home page
driver.find_element_by_xpath("//android.widget.RelativeLayout[5]").click()
driver.find_element_by_xpath("//android.widget.Button[@text='CONTINUE']").click()
driver.find_element_by_id("com.flipkart.android:id/custom_back_icon").click()
# Clicking on side menu
driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Drawer']").click()
# Go to laptop
driver.find_element_by_xpath("//android.widget.LinearLayout[4]").click()
driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout/"
                             "android.widget.LinearLayout/android.widget.TextView[3]").click()

# Scrolling using loop
for i in range(0, 4):
    touch = TouchAction(driver)
    touch.long_press(x=964, y=1726).move_to(x=956, y=280).release().perform()
    time.sleep(2)

driver.find_element_by_xpath("//android.widget.LinearLayout[2]/android.widget.FrameLayout/"
                             "android.widget.LinearLayout/android.widget.TextView[2]").click()
# Scrolling using uiautomator
driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector())."
                                           "scrollIntoView(text(\"Laptops\"))")
driver.find_element_by_xpath("//android.widget.TextView[@text='Laptops']")
driver.find_element_by_xpath("//android.widget.LinearLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/"
                             "android.view.ViewGroup/android.widget.LinearLayout[1]").click()
driver.find_element_by_id("com.flipkart.android:id/not_now_button").click()


# Filter result by price
driver.find_element_by_xpath("//android.widget.TextView[@text='Sort']").click()
driver.find_element_by_xpath("//android.widget.TextView[@text='Price -- High to Low']").click()
driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/"
                             "android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[1]/"
                             "android.widget.ImageView[1]").click()

# Screen scrolling
driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector())."
                                           "scrollIntoView(text(\"Seller Information\"))")


# Add to card and go to cart for assertion
driver.find_element_by_xpath("//android.widget.TextView[@text='ADD TO CART']").click()
driver.find_element_by_xpath("//android.widget.TextView[@text='GO TO CART']").click()
time.sleep(5)
price = driver.find_element_by_xpath("//android.view.ViewGroup/android.view.ViewGroup[1]/"
                                     "android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/"
                                     "android.view.ViewGroup[2]/android.view.ViewGroup/"
                                     "android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.TextView[1]").get_attribute('text')
print("The first mobile price is : " + price)

assert price == "₹70,731 ", "The test is failed"

# Save video to folder
video_raw = driver.stop_recording_screen()
video_name = driver.current_activity + time.strftime("%y_%m_%d_%H%M%S")
file_path = os.path.join("/Users/Jinal/PycharmProjects/AndroidAutomation/Screenshots" + video_name + ".mp4")

with open(file_path, "wb") as vd:
    vd.write(base64.b64decode(video_raw))

