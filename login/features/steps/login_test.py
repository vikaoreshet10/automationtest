import time
from behave import *
from selenium import webdriver


@given('open main page web player {portal}')
def step_impl(context, portal):
    context.browser = webdriver.Chrome('/usr/local/bin/chromedriver')
    context.browser.get(portal)


@then('write your user {login} and {password}')
def step_impl(context, login, password):
    time.sleep(5)
    context.browser.find_element_by_xpath('/html/body/div/div/div/form/div/input[1]').send_keys(login)
    time.sleep(5)
    context.browser.find_element_by_xpath('/html/body/div/div/div/form/div/input[2]').send_keys(password)


@then('click on button sing in')
def step_impl(context):
    time.sleep(5)
    context.browser.find_element_by_xpath('/html/body/div/div/div/form/div/input[3]').click()


@then('check login')
def step(context):
    context.browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/button').click()
    context.browser.quit()
