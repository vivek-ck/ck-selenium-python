from src.utils import BaseClass

class HomePage():

    __LEADS_TAB = "//a[@title='Leads']/.."

    def click_leads_tab(self, sb: BaseClass):
        sb.click(self.__LEADS_TAB)
        sb.sleep(2)