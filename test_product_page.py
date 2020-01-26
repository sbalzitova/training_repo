from .pages.product_page import ProductPage
import pytest


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()


def test_product_name_matches_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_product_name_match_product_name_in_basket()


def test_product_price_matches_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_product_price_match_price_in_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_guest_not_see_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_guest_not_see_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_success_message_dissapper()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_basket_be_empty()

