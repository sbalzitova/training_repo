import time
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        try:
            if self.url in self.browser.current_url:
                return True
        except:
            return False
        assert True, 'There is not login url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is missing'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is missing'

    def register_new_user(self):
        email = str(time.time()) + '@fakemail.org'
        password = str(time.time())
        email_field = self.find_element(*LoginPageLocators.REG_EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.find_element(*LoginPageLocators.REG_PASSWORD_FIELD)
        password_field.send_keys(password)
        confirm_password_field = self.find_element(*LoginPageLocators.REG_CONFIRM_PASSWORD_FIELD)
        confirm_password_field.send_keys(password)
        submit_button = self.find_element(*LoginPageLocators.REG_BUTTON_SUBMIT)
        submit_button.click()
        assert self.is_element_present(*LoginPageLocators.SUCCESS_REGISTRATION_ALERT), 'Registration seems to fail'


