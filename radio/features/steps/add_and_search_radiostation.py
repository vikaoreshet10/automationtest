import time
from behave import *
from selenium import webdriver


@given('open main page web player {portal}')
def step_impl(context, portal):
    context.browser = webdriver.Chrome('/usr/local/bin/chromedriver')
    context.browser.set_window_size(1024, 600)
    context.browser.maximize_window()
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


@then('click on tab radio')
def step_impl(context):
    time.sleep(3)
    context.browser.find_element_by_xpath('/html/body/div[1]/ul/li[5]/a').click()


@then('click on button add radiostation')
def step_impl(context):
    time.sleep(3)
    context.browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/div[1]/div/a').click()
    time.sleep(3)


@then('enter information')
def step_impl(context):
    time.sleep(3)
    context.browser.find_element_by_xpath(
        '/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/div/div[1]/div/div[2]/div/div[1]/input').send_keys(
        'Main Radiostation')
    context.browser.find_element_by_xpath(
        '/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/div/div[1]/div/div[3]/div/div[1]/input').send_keys(
        'http://air.radiorecord.ru:805/ibiza_320')


@then('click save')
def step_impl(context):
    time.sleep(3)
    context.browser.find_element_by_xpath(
        '/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/div/div[2]/div/div/div/div/div/button').click()


@then('search radiostation')
def step_impl(context):
    time.sleep(3)
    context.browser.find_element_by_xpath(
        '/html/body/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div[1]/label/input').send_keys(
        'Main Radiostation')
    time.sleep(5)
    context.browser.find_element_by_xpath(
        '/html/body/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div[1]/label/input').clear()
    context.browser.find_element_by_xpath(
        '/html/body/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div[1]/label/input').send_keys(
        'helloworld')
    time.sleep(5)
    x = context.browser.find_element_by_xpath(
        '/html/body/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/table/tbody/tr/td')
    assert x.text == 'Записи отсутствуют.'
    context.browser.quit()

# @then('delete radiostation')
# def step_impl(context):
# element = context.browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/table/tbody/tr/td[8]/div/a')
# time.sleep(3)
# hover = ActionChains(webdriver.Chrome()).move_to_element(element)
# hover.perform()
# parent = context.browser.find_element_by_xpath('html/body/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/table/tbody/tr')
# ActionChains(webdriver.Chrome()).move_to_element(parent).perform()
# time.sleep(1)

# action.move_to_element(parent_level_menu).perform()
# element.click()
# context.browser.find_element_by_xpath(
#   '/html/body/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/table/tbody/tr[1]/td[8]/div/ul/li[3]/a').click()
# context.browser.quit()
