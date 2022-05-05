from appium import webdriver

desired_caps = dict()

desired_caps['platformName'] = 'Android'

desired_caps['platformVersion'] = '7.1.2'

desired_caps['deviceName'] = 'emulator-5554'

desired_caps['appPackage'] = 'com.jiaozidt.appc'
desired_caps['appActivity'] = 'io.dcloud.PandoraEntryActivity'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['unicodekeyboard'] = True # 为了支持中文
desired_caps['resetKeyboard'] = True   # 设置成appium自带的键盘
desired_caps['noReset'] = True         # 使用缓存：绕过登录
# desired_caps[''] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.quit()




