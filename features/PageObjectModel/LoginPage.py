from selenium.webdriver.common.by import By

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
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_email_css).send_keys(email)

    def enter_login_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_password_css).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
        return AccountPage(self.driver)

    def display_status_of_No_match_for_email_address_and_or_Password(self, expected_msg):
        return self.driver.find_element(By.XPATH,
                                        self.No_match_for_email_address_and_or_Password_xpath).text.__contains__(
            expected_msg)
