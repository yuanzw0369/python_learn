from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from njpk_system_main.page.wrapper import handle_black


class BasePage:
    _driver = None
    _base_url = ''

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            options = Options()
            options.debugger_address = 'localhost:9222'
            self._driver = webdriver.Chrome(options=options)
            self._driver.implicitly_wait(3)

        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)
            sleep(2)

    @handle_black
    def find(self, locator, value: str = None):
        element: WebElement
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

    def finds(self, locator, value: str = None):
        element: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    def steps(self, path, name):
        with open(path, encoding="utf-8") as f:
            steps = yaml.safe_load(f)[name]
        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:
                    self.find(step["by"], step["locator"]).click()
                if "send" == action:
                    self.find(step["by"], step["locator"]).send_keys(step["value"])
                if "len > 0" == action:
                    eles = self.finds(step["by"], step["locator"])
                    return len(eles) > 0

    def wait_for_click(self, locator, time=10):
        WebDriverWait(self._driver, time).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_visible(self, locator, time=10):
        WebDriverWait(self._driver, time).until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_elem(self, condition, time=10):
        WebDriverWait(self._driver, time).until(condition)
