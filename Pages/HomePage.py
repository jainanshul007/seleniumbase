from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):


    '''Home page object'''

    EMAIL = (By.ID, "ap_email")
    SEARCHBOX = (By.ID, "twotabsearchtextbox")
    SEARCHBTN = (By.ID, "nav-search-submit-button")
