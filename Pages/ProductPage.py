from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Pages.RegisterPage import RegisterPage
from Pages.SearchPage import SearchPage


class ProductPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    add_to_cart_button_id = 'button-cart'
    added_to_cart_success_xpath = "//div[@class='alert alert-success alert-dismissible']"

    def add_product_to_cart(self):
        self.element_click("add_to_cart_button_id",self.add_to_cart_button_id)

    def retrieve_add_to_cart_message(self):
        return self.retrieve_element_text("added_to_cart_success_xpath",self.added_to_cart_success_xpath)