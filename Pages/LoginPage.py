from selenium.webdriver.common.by import By


from Config.config import TestData
from Pages.BasePage import BasePage

class LoginPage(BasePage):
    """Login page object or By locator"""
    EMAIL = (By.ID, "ap_email")
    PASSWORD = (By.ID, "ap_password")
    LOGIN_BTN = (By.ID, "signInSubmit")
    SIGNUP_LINKTXT = (By.LINK_TEXT, "Sign up")
    CONTINUE_BTN = (By.ID, "continue")
    CREATE_ACCOUNT_BTN = (By.ID, "createAccountSubmit")

    # """consturctor of page class"""

    def __init__(self, driver , app_url):
        # self.driver = driver
        super().__init__(driver)
        self.driver.get(app_url)

# """login page actions"""
#
# """get page title"""

    def get_login_page_title(self, title):
        return self.get_title(title)

# """this is used to check signup link"""

    def is_signup_button_visible(self):
        return self.is_visible(self.CREATE_ACCOUNT_BTN)

    # """login to application"""

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_click(self.CONTINUE_BTN)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BTN)
