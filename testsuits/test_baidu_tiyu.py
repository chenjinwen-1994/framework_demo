import unittest,time
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage
from pageobjects.baidu_news_home import newshomepage
from pageobjects.baidu_sp_home import tiyu_sp
class tiyu_sp_test(unittest.TestCase):
    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)
    def tearDown(self):
        self.driver.quit()
    def test_tiyu(self):
        #初始化百度首页
        baiduhome = HomePage(self.driver)
        baiduhome.news_click()
        #初始化体育页面
        newshome = newshomepage(self.driver)
        newshome.tiyulink()
        #初始化体育视频页面
        tiyuhome = tiyu_sp(self.driver)
        tiyuhome.tiyu_link()
        tiyuhome.get_windows_img()
if __name__ == '__main__':
    unittest.main()

