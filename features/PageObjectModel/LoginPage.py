from features.PageObjectModel.AccountPage import AccountPage
from features.PageObjectModel.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    textbox_email_css = 'input#input-email'
    textbox_password_css = 'input#input-password'
    button_login_xpath = "//input[@value='Login']"
    No_match_for_email_address_and_or_Password_xpath = "//div[contains(@class,'alert')]"

    def enter_login_email(self, email):
        self.type_into_field('textbox_email_css', self.textbox_email_css, email)

    def enter_login_password(self, password):
        self.type_into_field('textbox_password_css', self.textbox_password_css, password)

    def click_login_button(self):
        self.click_on_element('button_login_xpath', self.button_login_xpath)
        return AccountPage(self.driver)

    def display_status_of_No_match_for_email_address_and_or_Password(self, expected_msg):
        return self.retrieve_text_contains('No_match_for_email_address_and_or_Password_xpath',
                                           self.No_match_for_email_address_and_or_Password_xpath, expected_msg)
