from selenium.webdriver.common.by import By

from features.PageObjectModel.AccountCreatedPage import AccountCreatedPage
from features.PageObjectModel.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    firstname_xpath = '//input[@name="firstname"]'
    lastname_xpath = '//input[@name="lastname"]'
    email_xpath = '//input[@name="email"]'
    telephone_xpath = '//input[@name="telephone"]'
    password_xpath = '//input[@name="password"]'
    confirm_password_xpath = '//input[@name="confirm"]'
    privacy_policy_xpath = '//input[@name="agree"]'
    continue_button_xpath = "//input[contains(@class,'btn-primary')]"
    newsletter_subscribe_radio_button_xpath = '//label[@class="radio-inline"][1]/input'
    existing_email_warning_xpath = '//div[contains(@class,"alert")]'

    expected_privacy_policy_warning_xpath = '//div[contains(@class,"alert")]'
    expected_firstname_warning_xpath = '//input[@name="firstname"]/following-sibling::div'
    expected_lastname_warning_xpath = '//input[@name="lastname"]/following-sibling::div'
    expected_email_warning_xpath = '//input[@name="email"]/following-sibling::div'
    expected_telephone_warning_xpath = '//input[@name="telephone"]/following-sibling::div'
    expected_password_warning_xpath = '//input[@name="password"]/following-sibling::div'

    def enter_firstname(self, firstname):
        self.driver.find_element(By.XPATH, self.firstname_xpath).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.lastname_xpath).send_keys(lastname)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

    def enter_telephone(self, telephone):
        self.driver.find_element(By.XPATH, self.telephone_xpath).send_keys(telephone)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).send_keys(confirm_password)

    def click_on_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()
        return AccountCreatedPage(self.driver)

    def select_newsletter_subscribe_yes_radio_button(self):
        self.driver.find_element(By.XPATH, self.newsletter_subscribe_radio_button_xpath).click()

    def display_existing_email_warning(self, expected_warning):
        return self.driver.find_element(By.XPATH, self.existing_email_warning_xpath).text.__contains__(expected_warning)

    def select_privacy_policy_checkbox(self):
        self.driver.find_element(By.XPATH, self.privacy_policy_xpath).click()

    def privacy_policy_warning(self, expected_privacy_policy_warning):
        return self.driver.find_element(By.XPATH, self.expected_privacy_policy_warning_xpath).text.__eq__(
            expected_privacy_policy_warning)

    def firstname_warning(self, expected_firstname_warning):
        return self.driver.find_element(By.XPATH, self.expected_firstname_warning_xpath).text.__eq__(
            expected_firstname_warning)

    def lastname_warning(self, expected_lastname_warning):
        return self.driver.find_element(By.XPATH, self.expected_lastname_warning_xpath).text.__eq__(
            expected_lastname_warning)

    def email_warning(self, expected_email_warning):
        return self.driver.find_element(By.XPATH, self.expected_email_warning_xpath).text.__eq__(
            expected_email_warning)

    def telephone_warning(self, expected_telephone_warning):
        return self.driver.find_element(By.XPATH, self.expected_telephone_warning_xpath).text.__eq__(
            expected_telephone_warning)

    def password_warning(self, expected_password_warning):
        return self.driver.find_element(By.XPATH, self.expected_password_warning_xpath).text.__eq__(
            expected_password_warning)

    def all_warning_status(self, expected_privacy_policy_warning,
                           expected_firstname_warning,
                           expected_lastname_warning,
                           expected_email_warning,
                           expected_telephone_warning,
                           expected_password_warning):

        if self.privacy_policy_warning(expected_privacy_policy_warning) and \
                self.firstname_warning(expected_firstname_warning) and \
                self.lastname_warning(expected_lastname_warning) and \
                self.email_warning(expected_email_warning) and \
                self.telephone_warning(expected_telephone_warning) and \
                self.password_warning(expected_password_warning):

            return True

        else:
            return False
