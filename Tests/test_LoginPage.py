import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest

class Test_login(BaseTest):

    def test_create_account_button_visible(self , init_driver , app_url):
        self.login_page = LoginPage(init_driver , app_url)
        flag = self.login_page.is_signup_button_visible()
        assert flag

    def test_login_page_title(self , init_driver , app_url):
        self.login_page = LoginPage(init_driver , app_url)
        title = self.login_page.get_login_page_title(TestData.LOGINPAGE_TITLE)
        assert title

    def test_login(self , init_driver , app_url):
        self.login_page = LoginPage(init_driver , app_url)
        self.login_page.do_login(TestData.USER_NAME , TestData.PASSWORD)