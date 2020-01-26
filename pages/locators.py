from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn.btn-add-to-basket')
    SUCCESS_ALERT = (By.CLASS_NAME, 'alert-success')
    TOTAL_BASKET_VALUE_ALERT = (By.CLASS_NAME, 'alert-info')
    PRICE = (By.CLASS_NAME, 'price_color')
    NAME = (By.TAG_NAME, 'h1')
