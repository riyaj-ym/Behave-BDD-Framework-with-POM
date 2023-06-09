import time
from behave import *
from selenium.webdriver.common.by import By

from features.PageObjectModel.HomePage import HomePage
from features.PageObjectModel.SearchResultPage import SearchResultPage


@given(u'I got navigated to Home page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    exp_title = 'Your Store'
    assert context.home_page.verify_home_page_title(exp_title)


@when(u'I enter valid product into Search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_field('Hp')


@when(u'I click on Search button')
def step_impl(context):
    context.search_result_page = context.home_page.click_search_button()


@then(u'Valid product should get displayed in Search results')
def step_impl(context):
    assert context.search_result_page.display_status_of_valid_product()


@when(u'I enter invalid product into Search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_field("Honda")


@then(u'Proper message should be displayed in Search results')
def step_impl(context):
    expected_text = "There is no product that matches the search criteria."
    assert context.search_result_page.no_product_warning_message(expected_text)


@when(u'I don\'t enter any product into Search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_field('')
