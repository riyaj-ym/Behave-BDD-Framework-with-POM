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
        self.click_on_element('my_account_xpath', self.my_account_xpath)

    def click_on_login(self):
        self.click_on_element('login_link_text', self.login_link_text)
        return LoginPage(self.driver)

    def verify_home_page_title(self, exp_title):
        return self.driver.title.__eq__(exp_title)

    def enter_product_into_search_field(self, product):
        self.type_into_field('search_box_name', self.search_box_name, product)

    def click_search_button(self):
        self.click_on_element('search_button_css', self.search_button_css)
        return SearchResultPage(self.driver)

    def click_on_register(self):
        self.click_on_element('register_link_text', self.register_link_text)
        return RegisterPage(self.driver)
