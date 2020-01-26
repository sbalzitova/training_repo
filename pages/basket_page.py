from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_basket_be_empty(self):
        assert self.get_element_text(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE) == 'Your basket is empty. Continue shopping', \
            'Basket does not seem empty'
