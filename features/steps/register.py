import random
import string
from behave import *
from selenium.webdriver.common.by import By

from features.PageObjectModel.AccountCreatedPage import AccountCreatedPage
from features.PageObjectModel.HomePage import HomePage
from features.PageObjectModel.RegisterPage import RegisterPage


@given(u'I navigate to Register page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.register_page = context.home_page.click_on_register()


@when(u'I enter details into mandatory fields')
def step_impl(context):
    firstname = name(6)
    lastname = name(4)
    email = name(5) + "123@gmail.com"
    context.register_page.enter_firstname(firstname)
    context.register_page.enter_lastname(lastname)
    context.register_page.enter_email(email)
    context.register_page.enter_telephone('1234')
    context.register_page.enter_password('abc123')
    context.register_page.enter_confirm_password('abc123')


@when(u'I click on continue button')
def step_impl(context):
    context.account_created_page = context.register_page.click_on_continue_button()


@then(u'Account should get created')
def step_impl(context):
    expected_msg = "Your Account Has Been Created!"
    assert context.account_created_page.display_message_Your_account_has_been_created(expected_msg)


@when(u'I enter details into all fields')
def step_impl(context):
    firstname = name(6)
    lastname = name(4)
    email = name(5) + "123@gmail.com"

    context.register_page.enter_firstname(firstname)
    context.register_page.enter_lastname(lastname)
    context.register_page.enter_email(email)
    context.register_page.enter_telephone('1234')
    context.register_page.enter_password('abc123')
    context.register_page.enter_confirm_password('abc123')
    context.register_page.select_newsletter_subscribe_yes_radio_button()


@when(u'I enter details into all fields except email field')
def step_impl(context):
    firstname = name(6)
    lastname = name(4)

    context.register_page.enter_firstname(firstname)
    context.register_page.enter_lastname(lastname)
    context.register_page.enter_telephone('1234')
    context.register_page.enter_password('abc123')
    context.register_page.enter_confirm_password('abc123')
    context.register_page.select_newsletter_subscribe_yes_radio_button()


@when(u'I enter existing accounts email into email field')
def step_impl(context):
    context.register_page.enter_email('xofeger221@cutefier.com')


@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    expected_warning = 'Warning: E-Mail Address is already registered!'
    assert context.register_page.display_existing_email_warning(expected_warning)


@when(u'I dont enter any details in fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_firstname('')
    context.register_page.enter_lastname('')
    context.register_page.enter_email('')
    context.register_page.enter_telephone('')
    context.register_page.enter_password('')
    context.register_page.enter_confirm_password('')


@then(u'Proper warning messages for every mandatory fields should be displayed')
def step_impl(context):
    expected_privacy_policy_warning = "Warning: You must agree to the Privacy Policy!"
    expected_firstname_warning = "First Name must be between 1 and 32 characters!"
    expected_lastname_warning = "Last Name must be between 1 and 32 characters!"
    expected_email_warning = "E-Mail Address does not appear to be valid!"
    expected_telephone_warning = "Telephone must be between 3 and 32 characters!"
    expected_password_warning = "Password must be between 4 and 20 characters!"

    context.register_page = RegisterPage(context.driver)
    assert context.register_page.all_warning_status(expected_privacy_policy_warning, expected_firstname_warning,
                                                    expected_lastname_warning, expected_email_warning,
                                                    expected_telephone_warning, expected_password_warning)


@when(u'I select privacy policy checkbox')
def step_impl(context):
    context.register_page.select_privacy_policy_checkbox()


def name(n):
    chars = string.ascii_letters
    my_string = "".join(random.choice(chars) for _ in range(n))
    return my_string
