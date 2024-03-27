import pytest

from Pages.HomePage import HomePage
from tests.BaseTest import BaseTest
from Utilities import ExcelUtils


class TestRegister(BaseTest):
    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account(
            ExcelUtils.get_cell_data("ExcelFiles/TestData.xlsx","RegisterTest",2,1),
            ExcelUtils.get_cell_data("ExcelFiles/TestData.xlsx","RegisterTest",2,2),
            self.generate_email_with_time_stamp(),
            "1234567890",
            "1234567890","1234567890","no","select")
        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_heading_text)

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account("Shiv","Pratap",self.generate_email_with_time_stamp(),"1234567890","1234567890","1234567890","yes","select")
        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_heading_text)

    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("Shiv","Pratap","ShivPratap@gmail.com","1234567890","1234567890","1234567890","yes","select")
        expected_warning_message = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_duplicate_email_warning().__contains__(expected_warning_message)

    def test_enter_invalid_email_address(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("Shiv","Pratap","ShivPratap@gmail","1234567890","1234567890","1234567890","yes","select")
        expected_warning_message = "E-Mail Address does not appear to be valid!"
        assert register_page.retrieve_email_warning().__contains__(expected_warning_message)

    def test_different_password_in_confirm_password(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("Shiv","Pratap",self.generate_email_with_time_stamp(),"1234567890","1234567890","different","yes","select")
        expected_warning_message = "Password confirmation does not match password!"
        assert register_page.retrieve_confirm_password_warning().__contains__(expected_warning_message)

    @pytest.mark.parametrize("password", ExcelUtils.get_data_from_excel("ExcelFiles/TestData.xlsx", "ShortPassword"))
    def test_providing_short_password(self, password):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("Shiv", "Pratap", self.generate_email_with_time_stamp(), "1234567890",
                                          str(password[0]), str(password[0]), "yes", "select")

        expected_warning_message = "Password must be between 4 and 20 characters!"
        assert register_page.retrieve_password_warning().__contains__(expected_warning_message)


    # def test_enter_invalid_phone_number(self):
    #     home_page = HomePage(self.driver)
    #     register_page = home_page.navigate_to_register_page()
    #     account_success_page = register_page.register_an_account("Shiv", "Pratap",
    #                                                              self.generate_email_with_time_stamp(), "InvalidPhoneNumber",
    #                                                              "1234567890", "1234567890", "yes", "select")
    #     expected_heading_text = "Your Account Has Been Created!"
    #     assert not(account_success_page.retrieve_account_creation_message().__eq__(expected_heading_text))

    def test_register_without_privacy_policy(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("Shiv", "Pratap", self.generate_email_with_time_stamp(), "1234567890",
                                          "1234567890", "1234567890", "yes", "no")
        expected_warning_message = "Warning: You must agree to the Privacy Policy!"
        assert register_page.retrieve_privacy_policy_warning().__contains__(expected_warning_message)

    def test_register_without_entering_any_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("", "", "", "", "", "", "no", "no")
        assert register_page.verify_all_warnings("Warning: You must agree to the Privacy Policy!",
                                                 "First Name must be between 1 and 32 characters!",
                                                 "Last Name must be between 1 and 32 characters!",
                                                 "E-Mail Address does not appear to be valid!",
                                                 "Telephone must be between 3 and 32 characters!",
                                                 "Password must be between 4 and 20 characters!")
