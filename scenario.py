import json
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

page = "page"
mail_el = "mailbox_for_selenium@mail.ru"
password_el = "box123456"
submit = "//input[@type='submit']"

#
# # Test step 1 - Open URL
# def test_open_url():
#     browser = webdriver.Firefox()
#     browser.maximize_window()
#     browser.get("https://mail.ru")
#     assert "Mail.Ru" in browser.page_source
#     browser.quit()


# Test step 2 - Add credentials
def test_add_credentials():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get("https://mail.ru")
    browser.implicitly_wait(20)
    for line in browser.page_source:
        json.dump(line, 'file.txt')

    # mail = browser.find_element_by_xpath("id('mailbox__login')")
    # mail.send_keys(mail_el)
    # password = browser.find_element_by_xpath("id('mailbox__password')")
    # password.send_keys(password_el)
    # checker = browser.find_element_by_xpath("id('mailbox__auth__remember__checkbox')")
    # if checker:
    #     checker.click()
    # browser.find_element_by_xpath(submit).click()
    # browser.implicitly_wait(20)
    # browser.find_element_by_xpath("id('FooterLangSwitcher')").click()
    # browser.implicitly_wait(20)
    # select = Select(browser.find_element_by_xpath("id('langSwitcher')"))
    # select.select_by_value("en_US")
    # actions = browser.find_element_by_xpath("id('langSwitcher')").send_keys(
    #     Keys.TAB + Keys.TAB + Keys.ENTER)
    # browser.implicitly_wait(20)
    # browser.find_element_by_xpath("id('FooterLangSwitcher')").click()
    # browser.implicitly_wait(20)
    # select = Select(browser.find_element_by_xpath("id('langSwitcher')"))
    # select.select_by_value("ru_RU")
    # actions = browser.find_element_by_xpath("id('langSwitcher')").send_keys(
    #     Keys.TAB + Keys.TAB + Keys.ENTER)
    # browser.implicitly_wait(20)
    browser.quit()
# # Test step 3 - Submit form
# def test_submit_form(driver):
#     tests.submit_form(driver)
#
#
# # Test step 4 - verify URL
# def test_verify_url(driver, url):
#     tests.verify_url(driver, url)
