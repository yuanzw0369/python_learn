from selenium.webdriver.common.by import By
from njpk_system_main.page.base_page import BasePage
from njpk_system_main.page.user_manager import UserManager


class Admin(BasePage):

    def goto_user_manager(self):
        self.wait_for_click((By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/ul/li[1]/ul/div[5]/li/span'))
        self.find(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/ul/li[1]/ul/div[5]/li/span').click()
        return UserManager(self._driver)
