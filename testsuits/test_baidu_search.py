import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage
class BaiduSearh(unittest.TestCase):
    #这个方法每运行一次test都会打开浏览器再关闭
    # def setUp(self):
    #     browser = BrowserEngine(self)
    #     self.driver = browser.open_browser(self)
    # def tearDown(self):
    #     self.driver.quit()
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_baidusearch(self):
        '''
        这个self.driver，可以这样理解：在当前测试类里面，self.driver是来自浏览器引擎类中方法得到的，
        在初始化一个页面对象的时候，也把这个来自浏览器引擎类的driver给赋值给当前的页面对象，
        这样，才能执行页面对象或者基类里面的相关driver方法。
        :return:
        '''
        homepage = HomePage(self.driver)
        #调用页面对象方法
        homepage.search('selenium')
        homepage.search_click()
        time.sleep(3)
        #调用基类方法
        homepage.get_windows_img()
        self.assertIn('selenium',homepage.get_page_title(),'test fail')

    def test_baidusearch2(self):
        homepage = HomePage(self.driver)
        homepage.search('webdriver')
        homepage.search_click()
        time.sleep(3)
        homepage.get_windows_img()



if __name__ == '__main__':
    unittest.main()