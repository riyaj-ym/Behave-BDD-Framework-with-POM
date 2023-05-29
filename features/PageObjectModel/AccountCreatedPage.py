from features.PageObjectModel.BasePage import BasePage


class AccountCreatedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    your_account_has_been_created_message_xpath = '//div[@id="content"]/h1'

    def display_message_Your_account_has_been_created(self, expected_msg):
        return self.retrieve_text_equals('your_account_has_been_created_message_xpath',
                                         self.your_account_has_been_created_message_xpath, expected_msg)
