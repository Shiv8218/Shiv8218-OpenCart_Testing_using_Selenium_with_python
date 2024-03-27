from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Pages.RegisterPage import RegisterPage
from Pages.SearchPage import SearchPage


class CartPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    macbook_link_text = "MacBook"

    def validate_product_in_cart(self):
        self.check_display_status_of_element("macbook_link_text",self.macbook_link_text)