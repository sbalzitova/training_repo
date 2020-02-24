from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET = (By.CLASS_NAME, 'btn-group')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    REG_EMAIL_FIELD = (By.ID, 'id_registration-email')
    REG_PASSWORD_FIELD = (By.ID, 'id_registration-password1')
    REG_CONFIRM_PASSWORD_FIELD = (By.ID, 'id_registration-password2')
    REG_BUTTON_SUBMIT = (By.NAME, 'registration_submit')
    SUCCESS_REGISTRATION_ALERT = (By.CLASS_NAME, 'alert-success')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn.btn-add-to-basket')
    SUCCESS_ALERT = (By.CLASS_NAME, 'alert-success')
    NAME_IN_ALERT = (By.CSS_SELECTOR, '.alert-success > div > strong')
    PRICE_IN_ALERT = (By.CSS_SELECTOR, '.alert-info > div > p > strong')
    PRICE = (By.CSS_SELECTOR, 'p.price_color')
    NAME = (By.TAG_NAME, 'h1')


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
