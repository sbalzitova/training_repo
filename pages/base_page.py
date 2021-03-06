import math
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from .locators import BasketPageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket(self):
        link = self.browser.find_element(*BasePageLocators.BASKET)
        link.click()

    def find_element(self, how, what):
        element = self.browser.find_element(how, what)
        return element

    def should_basket_be_empty(self):
        assert self.get_element_text(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE) == 'Your basket is empty. Continue shopping', \
            'Basket does not seem empty'

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'Login link is not presented'

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def get_element_text(self, how, what):
        try:
            element = self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return element.text

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def should_be_authorized_user(self):
        assert self.is_element_present(
            *BasePageLocators.USER_ICON), 'User icon is not presented, probably unauthorised user'

# test function to pass Stepik tasks

# def solve_quiz_and_get_code(self):
#     alert = self.browser.switch_to.alert
#     x = alert.text.split(' ')[2]
#     answer = str(math.log(abs((12 * math.sin(float(x))))))
#     alert.send_keys(answer)
#     alert.accept()
#     time.sleep(5)
#     try:
#         alert = self.browser.switch_to.alert
#         alert_text = alert.text
#         print(f'Your code: {alert_text}')
#         alert.accept()
#     except NoAlertPresentException:
#         print('No second alert presented')
