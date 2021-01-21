import time
from selenium import webdriver


def loginForm(context):
    context.browser = webdriver.Chrome('/usr/local/bin/chromedriver')
    context.browser.get('http://10.110.51.251/player/')
    context.browser.find_element_by_xpath('/html/body/div[1]/div/div[5]/input').send_keys('12541')
    context.browser.find_element_by_xpath('/html/body/div[1]/div/div[6]/input').send_keys('1')
    time.sleep(5)
    context.browser.find_element_by_xpath('/html/body/div[1]/div/div[8]').click()
    time.sleep(5)
    context.browser.find_element_by_xpath('/html/body/div[1]/div/div[7]/input').send_keys('21957134FE09')
    context.browser.find_element_by_xpath('/html/body/div[1]/div/div[8]').click()