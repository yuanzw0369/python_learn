from time import sleep

from selenium import webdriver

from njpk_system_main.page.main import Main


class TestUserManage:
    def setup(self):
        self.main = Main()

    def test_add_user(self):
        add_user = self.main.goto_admin().goto_user_manager()
        add_user.add_user()
        assert add_user.get_user('R_bg671046fj')

