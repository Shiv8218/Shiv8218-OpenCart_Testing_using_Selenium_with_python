import pytest
from selenium.webdriver.common.by import By
from Pages.HomePage import HomePage
from tests.BaseTest import BaseTest


class TestAddToCart(BaseTest):

    def test_adding_product_from_display_page(self):
        home_page = HomePage(self.driver)
        product_page = home_page.click_on_product_from_home_page()
        product_page.add_product_to_cart()
        expected_message = "You have added"
        assert product_page.retrieve_add_to_cart_message().__contains__(expected_message)


