import logging

from selenium.webdriver.common.by import By


def handle_black(func):
    logging.basicConfig(level=logging.INFO)

    def wrapper(*args, **kwargs):
        from njpk_system_main.page.base_page import BasePage
        _black_list = [
            (By.XPATH,
             '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/form/div[1]/div/div/div/div/div/div[1]/span/span/i'),
            (By.XPATH,
             '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/form/div[13]/div/div/div/div/div/div/span/span/i'),
        ]
        _max_num = 2
        _error_num = 0
        instance: BasePage = args[0]
        try:
            logging.info("run" + func.__name__ + "\n args: \n" + repr(args) + "\n" + repr(kwargs))
            element = func(*args, **kwargs)
            _error_num = 0
            instance.set_implicitly(10)
            return element
        except Exception as e:
            instance.screenshot("tmp.png")
            logging.error("not found element, handle black list")
            instance.set_implicitly(10)
            if _error_num > _max_num:
                raise e
            _error_num += 1
            for ele in _black_list:
                elelist = instance.finds(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    return wrapper(*args, **kwargs)

            raise e

    return wrapper
