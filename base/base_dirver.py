from appium import webdriver


def init_driver():

    #server启动参数
    desired_caps = {}
    #设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] ='5.1'
    desired_caps['deviceName'] = '192.168.x.x:端口号' #iOS用到 这里Android也定义上可以随便写参数
    #app信息 (包名、启动名)
    desired_caps['appPackage'] ='com.android.settings'
    desired_caps['appActivity'] ='.Settings'
    #中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # appium服务
    driver = webdriver.Remote('http://localhost:4732/wd/hu',desired_caps)

