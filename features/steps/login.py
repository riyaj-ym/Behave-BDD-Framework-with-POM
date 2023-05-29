import random
import string
from behave import *
from selenium.webdriver.common.by import By

from features.PageObjectModel.AccountPage import AccountPage
from features.PageObjectModel.HomePage import HomePage
from features.PageObjectModel.LoginPage import LoginPage


@given(u'I navigated to Login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.login_page = context.home_page.click_on_login()


@when(u'I enter valid email and valid password into the fields')
def step_impl(context):
    context.login_page.enter_login_email('xofeger221@cutefier.com')
    context.login_page.enter_login_password('yFkp58tn6U@s')


@when(u'I clicked on Login button')
def step_impl(context):
    context.account_page = context.login_page.click_login_button()


@then(u'I should get logged in')
def step_impl(context):
    assert context.account_page.display_status_of_edit_your_account_information_option()


@when(u'I enter invalid email and valid password into the fields')
def step_impl(context):
    invalid_email = generate_email(5) + "@gmail.com"
    context.login_page.enter_login_email(invalid_email)
    context.login_page.enter_login_password('yFkp58tn6U@s')


@then(u'I should get proper warning message')
def step_impl(context):
    expected_msg = "Warning: No match for E-Mail Address and/or Password."
    assert context.login_page.display_status_of_No_match_for_email_address_and_or_Password(expected_msg)


@when(u'I enter valid email and invalid password into the fields')
def step_impl(context):
    invalid_password = generate_pass(8)
    context.login_page.enter_login_email('xofeger221@cutefier.com')
    context.login_page.enter_login_password(invalid_password)


@when(u'I enter invalid email and invalid password into the fields')
def step_impl(context):
    invalid_email = generate_email(5) + "@gmail.com"
    invalid_password = generate_pass(8)
    context.login_page.enter_login_email(invalid_email)
    context.login_page.enter_login_password(invalid_password)


@when(u'I dont enter any email and password into the fields')
def step_impl(context):
    context.login_page.enter_login_email('')
    context.login_page.enter_login_password('')


def generate_email(size):
    characters = string.ascii_letters + string.digits
    my_string = "".join(random.choice(characters) for _ in range(size))
    return my_string


def generate_pass(size):
    characters = string.ascii_letters + string.digits + string.punctuation
    my_string = "".join(random.choice(characters) for _ in range(size))
    return my_string
