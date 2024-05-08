from time import sleep
from selenium.webdriver.common.by import By

from njpk_system_main.page.admin_page import Admin
from njpk_system_main.page.base_page import BasePage


class Main(BasePage):
    _base_url = 'https://std.ahtelit.com/dist/#/home/index'

    def goto_admin(self):
        self.wait_for_click((By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/div[2]/ul/li[3]/span'))
        self.find(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/div[2]/ul/li[3]/span').click()
        return Admin(self._driver)
