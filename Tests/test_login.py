import time

import pytest
from selenium.webdriver import ActionChains, Keys

import resources
from Tests import readCreds
from pageObjects.login_page import loginPage
from pageObjects.resource_page import resourcePage


@pytest.fixture
def test_loginToAlkermies(driver):
    # Open Browser
    login_page = loginPage(driver)
    # # Navigate to Site URL
    login_page.open()
    # # Login to the page
    login_page.perform_login()
    login_page.click_Aristada_IDN()
    login_page.click_goBtn()



def test_checkLinksInPdf(driver, test_loginToAlkermies):

    resource_page = resourcePage(driver)
    # # Give the resource id here
    resource = resources.resource1
    resource_page.send_textInSearch(resource)
    resource_page.click_eye()
    resource_page.total_links()
    resource_page.hit_links()



