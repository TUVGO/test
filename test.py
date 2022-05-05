from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android' # 打开什么平台的app 固定的 > 启动安卓平台
desired_caps['platformVersion'] = '7.1.2' # 安卓系统的版本号： adb shell getprop ro.build.version.release   
desired_caps['deviceName'] = 'SM-N9760' # 手机、模拟器的型号：adb shell getprop ro.product.model
desired_caps['appPackage'] = 'com.jiaozidt.appc'  # app的名字
                                                      # 安卓8.1之前：adb shell dumpsys activity | findstr "mFocuseActivity" 
                                                      # 1.adb shell 2. dumpsys activity | grep mFocusedActivity

                                                      # 安卓8.1之后：adb shell dumpsys activity | findstr "mResume"

desired_caps['appActivity'] = 'com.ss.android.ugc.aweme.splash.SplashActivity' # 同上
desired_caps['unicodekeyboard'] = True # 为了支持中文
desired_caps['resetKeyboard'] = True   # 设置成appium自带的键盘
desired_caps['noReset'] = True         # 使用缓存：绕过登录

# 打开app，并且返回当前app的操作对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


