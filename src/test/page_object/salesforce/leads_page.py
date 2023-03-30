from src.utils.base_class import BaseClass

class SalesforceLeadsPage(BaseClass):
    NEW_LEAD = "//a/div[@title='New']"
    LEAD_MODAL_HEADER = "//div/h2[contains(text(), 'New Lead')]"
    SALUTATION_DROPBOX = "//label[contains(text(), 'Salutation')]/following-sibling::div"
    FIRST_NAME = "//input[@name='firstName']"
    MIDDLE_NAME = "//input[@name='middleName']"
    LAST_NAME = "//input[@name='lastName']"
    COMPANY_NAME = "//input[@name='Company']"
    SEARCH_ADDRESS_TEXT = "//input[@placeholder='Search Address']"
    SAVE_LOAN_BUTTON = "//button[@name='SaveEdit']"
    LEAD_SEARCH_BOX = "//input[@name='Lead-search-input']"
    SALUTATION_VALUES = "//span[@title='{}']/ancestor::lightning-base-combobox-item"
    ADDRESS_SEARCH_VALUE = "//lightning-base-combobox-formatted-text[@title='{}']/.."
    LEAD_SEARCH_RESULTS = "//table[@role='grid']/tbody/tr"

    def initiate_lead(sb):
        sb.wait_for_element_clickable(SalesforceLeadsPage.NEW_LEAD)
        sb.click(SalesforceLeadsPage.NEW_LEAD)

    def create_lead(sb, salutation_string, last_name_string, company_name_string):
        sb.click(SalesforceLeadsPage.SALUTATION_DROPBOX)
        sb.click(SalesforceLeadsPage.SALUTATION_VALUES.format(salutation_string))
        sb.type(SalesforceLeadsPage.LAST_NAME, last_name_string)
        sb.scroll_to_element(SalesforceLeadsPage.COMPANY_NAME)
        sb.type(SalesforceLeadsPage.COMPANY_NAME, company_name_string)
        sb.click(SalesforceLeadsPage.SAVE_LOAN_BUTTON)
        sb.sleep(5)

    def validate_lead(sb, last_name_string):
        sb.type(SalesforceLeadsPage.LEAD_SEARCH_BOX, last_name_string + "\n")
        sb.sleep(5)
        sb.assert_element_visible(SalesforceLeadsPage.LEAD_SEARCH_RESULTS)
