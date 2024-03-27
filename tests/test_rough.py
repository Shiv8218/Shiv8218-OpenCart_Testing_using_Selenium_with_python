import time

import pytest

from Pages.HomePage import HomePage
from tests.BaseTest import BaseTest
from Utilities import ExcelUtils


class TestRegister(BaseTest):
    def test_register_without_privacy_policy(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("Shiv", "Pratap", self.generate_email_with_time_stamp(), "1234567890",
                                          "1234567890", "1234567890", "yes", "no")
        expected_warning_message = "Warning: You must agree to the Privacy Policy!"
        assert register_page.retrieve_privacy_policy_warning().__contains__(expected_warning_message)