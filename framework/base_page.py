import time,os
from selenium.common.exceptions import NoSuchElementException
from framework.logger import Logger
logger = Logger(logger='BasePage').getlog()
class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """
    def __init__(self,driver):
        self.driver = driver
    def quit_browser(self):
        self.driver.quit()
    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)
        logger.info('隐式等待%s秒'%seconds)
    def forward(self):
        self.driver.forward()
    def back(self):
        self.driver.back()
    #关闭当前页面窗口
    def close_browser(self):
        try:
            self.driver.close()
            logger.info('关闭页面成功')
        except NameError as e:
            logger.error('关闭当前页面失败:%s'%e)
    #截图
    def get_windows_img(self):
        file_path = os.path.dirname(os.getcwd())+'/framework_demo/screenshots/'
        rq = time.strftime('%Y-%m-%d_%H.%M.%S')
        filename = file_path+rq+'.jpg'
        try:
            self.driver.get_screenshot_as_file(filename)
            logger.info('截图成功保存在screenshots目录下')
        except NameError as e:
            logger.error('截图失败：%s'%e)
    #定位元素
    def find_element(self,selector):
        """
        这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
        submit_btn = "id=>su"
        login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
        如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        #切割selector
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        if selector_by =='id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info('成功定位到元素')
            except NoSuchElementException as e:
                logger.error('定位失败：%s'%e)
                #截图
                self.get_windows_img()
        elif selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info('成功定位到元素')
            except NoSuchElementException as e:
                logger.error('定位失败：%s'%e)
                #截图
                self.get_windows_img()
        #其他异常处理用的不多故没写,可补齐
        elif selector_by =='name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by =='class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by =='link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by =='partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by =='tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by =='selector_selector':
            element = self.driver.find_element_by_selector_selector(selector_value)
        else:
            #引发异常
            raise NameError('请检查元素是否有效、可见')
        return element

    #清空
    def clear(self,selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info('清空')
        except NameError as e:
            logger.error('清空失败%s'%e)
            self.get_windows_img()

    #输入
    def type(self,selector,text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info('成功输入：%s'%text)
        except NameError as e:
            logger.error('输入失败：%s'%e)
            self.get_windows_img()
    #点击
    def click(self,selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info('点击元素')
        except NameError as e:
            logger.error('点击元素失败%s'%e)
    #获取页面标题
    def get_page_title(self):
        title = self.driver.title
        return title
        logger.info('当前页面标题是%s'%title)





