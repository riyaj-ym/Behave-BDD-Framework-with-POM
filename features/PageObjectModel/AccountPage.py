from selenium.webdriver.common.by import By

from features.PageObjectModel.BasePage import BasePage


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    edit_your_account_information_option_xpath = "//a[text()='Edit your account information']"

    def display_status_of_edit_your_account_information_option(self):
        return self.driver.find_element(By.XPATH, self.edit_your_account_information_option_xpath).is_displayed()
