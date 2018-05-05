#浏览器引擎类
import configparser,time,os
from selenium import webdriver
from framework.logger import Logger
logger = Logger(logger='BrowserEngine').getlog()
class BrowserEngine(object):
    # dir = os.path.dirname(os.path.abspath(''))
    def __init__(self,driver):
        self.driver = driver
    def open_browser(self,driver):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.getcwd())+'/framework_demo/config/config.ini'
        config.read(file_path)

        browser = config.get('browserType','browserName')
        logger.info('you have select %s browser'%browser)
        url = config.get('testServer','URL')
        logger.info('test url is: %s'%url)

        if browser == 'Firefox':
            driver = webdriver.Firefox()
            logger.info('starting Firefox browser ')
        elif browser == 'Chrome':
            driver = webdriver.Chrome()
            logger.info('starting Chrome browser ')
        elif browser == 'Ie':
            driver = webdriver.Ie()
            logger.info('staring Ie browser')

        driver.get(url)
        logger.info('open %s'%url)
        driver.maximize_window()
        logger.info('max browser')
        driver.implicitly_wait(5)
        return driver
    def quit_browser(self):
        self.driver.quit()
        logger.info('close browser')



