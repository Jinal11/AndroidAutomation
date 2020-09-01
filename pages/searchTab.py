"""
Page created by Jinal Shah
Wrote test case for search bar

"""

from appium import webdriver
import time

desired_cap = {
    "deviceName": "29d5d20a0104",
    "platformName": "Android",
    "appPackage": "com.flipkart.android",
    "appActivity": "com.flipkart.android.activity.HomeFragmentHolderActivity",
    "automationName": "UiAutomator2"

}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

# Go to main screen
driver.find_element_by_xpath("//android.widget.RelativeLayout[5]").click()
driver.find_element_by_xpath("//android.widget.Button[@text='CONTINUE']").click()
driver.find_element_by_id("com.flipkart.android:id/custom_back_icon").click()

# Searchbar actions
driver.find_element_by_id("com.flipkart.android:id/search_widget_textbox").click()
driver.find_element_by_id("com.flipkart.android:id/search_autoCompleteTextView").send_keys("Airpods")
driver.execute_script('mobile:performEditorAction', {'action': 'search'})
driver.find_element_by_id("com.flipkart.android:id/not_now_button").click()

# Take Screenshots
fileName = driver.current_activity + time.strftime("%y_%m_%d_%H%M%S")
time.sleep(5)
driver.save_screenshot("/Users/Jinal/PycharmProjects/AndroidAutomation/Screenshots/" + "laptop" + fileName + ".png")

