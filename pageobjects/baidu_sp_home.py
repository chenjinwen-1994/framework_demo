from framework.base_page import BasePage

class tiyu_sp(BasePage):
    tiyu_link_s = 'link_text=>体育视频'
    def tiyu_link(self):
        self.click(self.tiyu_link_s)
