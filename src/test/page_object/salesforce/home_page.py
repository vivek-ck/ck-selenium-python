from src.utils.base_class import BaseClass

class SalesforceHomePage(BaseClass):

    LEADS_TAB = "//a[@title='Leads']/.."

    def click_leads_tab(sb):
        sb.click(SalesforceHomePage.LEADS_TAB)
        sb.sleep(2)