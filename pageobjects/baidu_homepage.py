from framework.base_page import BasePage
class HomePage(BasePage):
    '''
    页面对象中，百度主页的元素定位和简单的操作函数，页面类主要是元素定位和页面操作写成函数，供测试类调用
    '''
    #元素定位写法，=>和base_page.py中find_element()方法元素定位切割有关系
    input_box = "id=>kw"
    search_btn = "xpath=>//*[@id='su']"
    news = "link_text=>新闻"

    def search(self,text):
        self.type(self.input_box,text)

    def search_click(self):
        self.click(self.search_btn)

    def news_click(self):
        self.click(self.news)