from behave import *
import time

from selenium.webdriver.chrome import webdriver


@given('I am login in web player {portal} and {login} and {password} and {licenses}')
def login(context, portal, login, password, licenses):
    context.browser = webdriver.Chrome('/usr/local/bin/chromedriver')
    context.browser.get(portal)
    context.browser.find_element_by_xpath('/html/body/div[1]/div/div[5]/input').send_keys(login)
    context.browser.find_element_by_xpath('/html/body/div[1]/div/div[6]/input').send_keys(password)
    time.sleep(5)
    context.browser.find_element_by_xpath('/html/body/div[1]/div/div[8]').click()
    time.sleep(5)
    context.browser.find_element_by_xpath('/html/body/div[1]/div/div[7]/input').send_keys(licenses)
    context.browser.find_element_by_xpath('/html/body/div[1]/div/div[8]').click()


@then('Select channel from the list')
def select(context):
    time.sleep(5)
    context.browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[18]/div').click()


@then('Press button Play')
def play(context):
    time.sleep(5)
    context.browser.find_element_by_xpath('//*[@id="vjs_video_3"]/div[4]/button[1]').click()
    time.sleep(5)


@then('Check TV guide')
def tvguide(context):
    x = context.browser.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div[2]/div')
    assert x.text == 'Т/с Агенти справедливості, 6 сезон'
