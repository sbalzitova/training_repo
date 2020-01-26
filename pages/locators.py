from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn.btn-add-to-basket')
    SUCCESS_ALERT = (By.CLASS_NAME, 'alert-success')
    NAME_IN_ALERT = (By.CSS_SELECTOR, '.alert-success > div > strong')
    PRICE_IN_ALERT = (By.CSS_SELECTOR, '.alert-info > div > p > strong')
    PRICE = (By.CSS_SELECTOR, 'p.price_color')
    NAME = (By.TAG_NAME, 'h1')
