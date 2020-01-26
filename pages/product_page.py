from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        login_link.click()

    def should_product_name_match_product_name_in_basket(self):
        assert self.get_element_text(*ProductPageLocators.NAME) == self.get_element_text(*ProductPageLocators.NAME_IN_ALERT), 'Name in alert does not match product'

    def should_product_price_match_price_in_basket(self):
        assert self.get_element_text(*ProductPageLocators.PRICE) == self.get_element_text(*ProductPageLocators.PRICE_IN_ALERT), 'Price in alert does not match product'







