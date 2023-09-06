import time

import pytest
from selenium.webdriver import ActionChains, Keys

import resources
from pageObjects.login_page import loginPage
from pageObjects.resource_page import resourcePage


@pytest.fixture
def test_loginToAlkermies(driver):
    # Open Browser
    login_page = loginPage(driver)
    # Navigate to Site URL
    login_page.open()
    # Login to the page
    # username = readCreds.read_data(2, 1)
    # password = readCreds.read_data(2, 2)
    login_page.perform_tradelogin()
    login_page.click_aristasaCheckOne()
    login_page.click_goBtn()



def test_checkLinksInPdf(driver, test_loginToAlkermies):

    resource_page = resourcePage(driver)
    resource = resources.resource1
    resource_page.send_textInSearch(resource)
    resource_page.click_eye()
    resource_page.total_links()
    resource_page.click_links()


