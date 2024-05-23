from selenium.webdriver.common.by import By

from njpk_system_main.page.base_page import BasePage


class UserManager(BasePage):

    def add_user(self):
        # 点击添加访问用户
        self.wait_for_click((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/button/span'))
        self.find(By.XPATH,
                  '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/button/span').click()

        # 点击角色选择框
        def wait_select_rule(x):
            elements_len = len(self.finds(By.XPATH, '/html/body/div[3]'))
            if elements_len <= 0:
                self.find(By.XPATH,
                          '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/form/div[1]/div/div/div/div/div/div[1]/span/span/i').click()
            return elements_len > 0

        self.wait_for_elem(wait_select_rule)
        self.find(By.XPATH,
                  '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/form/div[1]/div/div/div/div/div/div[1]/span/span/i').click()

        # 勾选角色
        self.wait_for_click((By.XPATH,
                             '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/form/div[13]/div/div/div/div/div/div/input'))
        self.find(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div[1]/ul/li[4]/label/span/span').click()

        # 输入账号
        self.find(By.XPATH,
                  '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/form/div[3]/div/div/div/label').click()
        self.find(By.XPATH,
                  '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/form/div[2]/div/div/div/div/div[1]/input').send_keys(
            'test9001')

        # 输入姓名
        self.find(By.XPATH,
                  '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/form/div[3]/div/div/div/div/div/input').send_keys(
            '测试9001')

        # 点击行政区划选择框
        def wait_select_area(x):
            elements_len = len(self.finds(By.XPATH, '/html/body/div[4]/div[1]/div/div[1]/ul'))
            if elements_len <= 0:
                self.find(By.XPATH,
                          '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/form/div[13]/div/div/div/div/div/div/span/span/i').click()
            return elements_len > 0

        self.wait_for_elem(wait_select_area)
        # self.wait_for_visible((By.XPATH,
        #                        '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/form/div[13]/div/div/div/div/div/div/span/span/i'))
        # self.wait_for_click((By.XPATH,
        #                      '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/form/div[13]/div/div/div/div/div/div/span/span/i'))
        self.find(By.XPATH,
                  '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/form/div[13]/div/div/div/div/div/div/span/span/i').click()

        # 勾选行政区划
        self.wait_for_click((By.XPATH, '/html/body/div[4]/div[1]/div/div[1]/ul/li/span'))
        self.find(By.XPATH, '/html/body/div[4]/div[1]/div/div[1]/ul/li/label/span[1]/span').click()
        # 点击确定
        self.wait_for_click(
            (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div/div/div[3]/span/button[2]'))
        self.find(By.XPATH,
                  '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div/div/div[3]/span/button[2]').click()
        # self._driver.quit()

    def get_user(self, value):
        self.wait_for_click((By.XPATH,
                             '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[8]/div/div/span[2]'))
        cur_page = int(self.find(By.XPATH,
                                 '/html/body/div/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[3]/slot/span/span[2]/span[1]/span').text)
        total_page = int(self.find(By.XPATH,
                                   '/html/body/div/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[3]/slot/span/span[2]/span[2]/span').text)

        while True:
            elements = self.finds(By.CSS_SELECTOR, '.cell-class-name:nth-child(2)')
            for element in elements:
                if value == element.get_attribute("innerText"):
                    return True
            cur_page = int(self.find(By.XPATH,
                                     '/html/body/div/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[3]/slot/span/span[2]/span[1]/span').text)
            if cur_page == total_page:
                return False

            def wait_user_details(x):
                elements_len = len(
                    self.finds(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div/div/div[1]/span'))
                if elements_len <= 0:
                    self.find(By.XPATH,
                              '/html/body/div/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[1]').click()
                return elements_len > 0

            self.wait_for_elem(wait_user_details)
            # self.wait_for_click(
            #     (By.XPATH,
            #      '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[8]/div/div/span[2]'))
            self.find(By.XPATH,
                      '/html/body/div/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[3]/div/button[2]').click()

    def search_user(self):
        self.find(By.XPATH,
                  '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/input').send_keys(
            "测试9001")
        self.wait_for_visible(
            (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[1]/button[1]'))
        self.wait_for_click((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[1]/button[1]'))
        self.find(By.XPATH,
                  '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[1]/button[1]').click()
