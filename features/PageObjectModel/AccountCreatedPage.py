from selenium.webdriver.common.by import By

from features.PageObjectModel.BasePage import BasePage


class AccountCreatedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    your_account_has_been_created_message_xpath = '//div[@id="content"]/h1'

    def display_message_Your_account_has_been_created(self, expected_msg):
        return self.driver.find_element(By.XPATH, self.your_account_has_been_created_message_xpath).text.__eq__(
            expected_msg)
