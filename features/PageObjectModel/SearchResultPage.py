from selenium.webdriver.common.by import By

from features.PageObjectModel.BasePage import BasePage


class SearchResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    valid_product_link_text = 'HP LP3065'
    no_product_warning_xpath = '//input[@id="button-search"]/following-sibling::p'

    def display_status_of_valid_product(self):
        return self.driver.find_element(By.LINK_TEXT, self.valid_product_link_text).is_displayed()

    def no_product_warning_message(self, expected_warning):
        return self.driver.find_element(By.XPATH, self.no_product_warning_xpath).text.__eq__(expected_warning)
