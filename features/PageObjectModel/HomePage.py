from selenium.webdriver.common.by import By

from features.PageObjectModel.BasePage import BasePage
from features.PageObjectModel.LoginPage import LoginPage
from features.PageObjectModel.RegisterPage import RegisterPage
from features.PageObjectModel.SearchResultPage import SearchResultPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    my_account_xpath = '//span[text()="My Account"]'
    login_link_text = 'Login'
    search_box_name = 'search'
    search_button_css = 'button.btn-default'
    register_link_text = 'Register'

    def click_on_my_account(self):
        self.driver.find_element(By.XPATH, self.my_account_xpath).click()

    def click_on_login(self):
        self.driver.find_element(By.LINK_TEXT, self.login_link_text).click()
        return LoginPage(self.driver)

    def verify_home_page_title(self, exp_title):
        return self.driver.title.__eq__(exp_title)

    def enter_product_into_search_field(self, product):
        self.driver.find_element(By.NAME, self.search_box_name).send_keys(product)

    def click_search_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.search_button_css).click()
        return SearchResultPage(self.driver)

    def click_on_register(self):
        self.driver.find_element(By.LINK_TEXT, self.register_link_text).click()
        return RegisterPage(self.driver)
