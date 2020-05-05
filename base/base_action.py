from selenium.webdriver.support.wait import WebDriverWait
class BaseAction:
    def __init__(self,driver):   #创建对象的时候就直接可以使用driver
        self.driver=driver
    def find_element(self,loc):
      by = loc[0]
      value = loc[1]
      return WebDriverWait(self.driver,5,1).until(lambda x:x.find_element(by,value))
    def click(self,loc):            #点击
        self.find_element(loc).click()
    def input_text(self,loc,text):    #输入
        self.find_element(loc).send_keys(text)