from framework.base_page import BasePage

class newshomepage(BasePage):
    tiyu_link = 'link_text=>体育'
    def tiyulink(self):
        self.click(self.tiyu_link)
        