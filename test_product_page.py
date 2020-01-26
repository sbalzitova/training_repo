from .pages.product_page import ProductPage
import pytest
import time


# @pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9'])
# def test_guest_can_add_product_to_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#
#
# @pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6',
#                                   pytest.param('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7', marks=pytest.mark.xfail),
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9'])
# def test_product_name_matches_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.should_product_name_match_product_name_in_basket()
#
#
# @pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8',
#                                   'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9'])
# def test_product_price_matches_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.should_product_price_match_price_in_basket()


# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.should_guest_not_see_success_message()
#
#
# def test_guest_cant_see_success_message(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_guest_not_see_success_message()
#
#
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     page = ProductPage(browser, link)
#     page.open()
#     time.sleep(1)
#     page.add_to_basket()
#     page.should_success_message_dissapper()


def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page (browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
