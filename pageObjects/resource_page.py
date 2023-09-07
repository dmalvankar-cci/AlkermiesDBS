import time

import requests
from colorama import Fore, Back
from selenium.webdriver import Keys
from termcolor import colored

from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class resourcePage:


    __treatment = (By.XPATH, "//a[normalize-space()='Treatment']")
    __patient_population = (By.XPATH, "//a[@href='#collapse-18']")
    __all_links = (By.XPATH, "//section[@class='linkAnnotation']/a")
    __next_page = (By.XPATH, "//button[@id='next']")
    __pages = (By.XPATH, "//input[@id='pageNumber']")
    __pageNumberBox = (By.XPATH, "//input[@id='pageNumber']")
    __searchBar = (By.XPATH, "//input[@placeholder='Search']")
    # __aristada = (By.XPATH, "//a[@id='id-ARISTADA']")
    __eye = (By.XPATH, "//span[@class='mat-tooltip-trigger icons']//i[@class='fa fa-eye']")
    __patient_population_branded = (By.XPATH, "(//div[@class='mat-tab-label-content'][normalize-space()='BRANDED'])[2]")
    __eye_view = (By.XPATH, "//body[1]/app-root[1]/div[1]/dbc-basic-layout[1]/main[1]/dbc-resources[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/mat-tab-group[1]/div[1]/mat-tab-body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]/span[1]/i[1]")
    __treatment_branded = (By.XPATH, "//div[@id='mat-tab-label-2-1']//div[@class='mat-tab-label-content'][normalize-space()='BRANDED']")
    # __pdf_id = (By.XPATH, "//small[@class='text-red-100 pl-3']")
    def __init__(self, driver: WebDriver):
        self._driver = driver


    @property
    def current_url(self):
        return self._driver.current_url


    def click_treatment_branded(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__treatment_branded))
        self._driver.find_element(*self.__treatment_branded).click()
    def click_patient_population_branded(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__patient_population_branded))
        self._driver.find_element(*self.__patient_population_branded).click()


    def click_patient_population(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__patient_population))
        self._driver.find_element(*self.__patient_population).click()

    def click_treatment(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__treatment))
        self._driver.find_element(*self.__treatment).click()



    def click_next(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__next_page))
        Page_count = self._driver.find_element(*self.__pages).get_attribute("max")
        page_count_int = int(Page_count)
        for page_count_int in range(1, page_count_int):
            next_btnClick = self._driver.find_element(*self.__next_page)
            next_btnClick.click()



    def click_eye(self):
        wait = WebDriverWait(self._driver, 15)
        wait.until(ec.visibility_of_element_located(self.__eye))
        self._driver.find_element(*self.__eye).click()



    def send_textInSearch(self, resource):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__searchBar))
        self._driver.find_element(*self.__searchBar).send_keys(resource)
        self._driver.find_element(*self.__searchBar).send_keys(Keys.ENTER)



    def total_links(self):
        time.sleep(10)
        wait = WebDriverWait(self._driver, 50)
        wait.until(ec.visibility_of_element_located(self.__pages))
        Page_count = self._driver.find_element(*self.__pages).get_attribute("max")
        page_count_int = int(Page_count)
        for page_count_int in range(1, page_count_int):
            wait = WebDriverWait(self._driver, 50)
            wait.until(ec.visibility_of_element_located(self.__next_page))
            next_btnClick = self._driver.find_element(*self.__next_page)
            next_btnClick.click()
        # wait = WebDriverWait(self._driver, 20)
        # wait.until(ec.visibility_of_all_elements_located(self.__all_links))
        links = self._driver.find_elements(*self.__all_links)
        print("No of links found:", len(links))





    # def get_pdf_id(self):
    #     wait = WebDriverWait(self._driver, 10)
    #     wait.until(ec.presence_of_all_elements_located(self.__pdf_id))
    #     pdfs = self._driver.find_elements(*self.__pdf_id)
    #     for pdf in pdfs:
    #         if pdf.text != "":
    #             return pdf.text



    def hit_links(self):
        Number = 1
        wait = WebDriverWait(self._driver, 30)
        wait.until(ec.presence_of_all_elements_located(self.__all_links))
        links = self._driver.find_elements(*self.__all_links)
        for link in links:
            # link.click()
            href = link.get_attribute("href")
            r = requests.get(href)
            if href == None:
                print(f"Url is having Null value")
                print(f"-------------------------")

            elif href.startswith('http'):
                try:
                    print(Number, ":", r.status_code, r.reason)
                    Number += 1
                    if r.status_code >= 400:
                        print(f"External Broken Link:", {href})
                        print(f"------------------------------")
                    else:
                        print(f"Correct External links:", {href})
                        print(f"------------------------------")
                except requests.exceptions.RequestException:
                    print(Number, ":", f"Error checking External link:", {href})
                    Number += 1
                    print(f"------------------------------")
            else:
                try:
                    r = requests.get(href)
                    print(Number, ":", r.status_code, r.reason)
                    Number += 1
                    if r.status_code >= 400:
                        print("Internal Broken Link:", {href})
                        print(f"------------------------------")
                    else:
                        print(f"Correct Internal links:", {href})
                        print(f"------------------------------")
                except requests.exceptions.RequestException:
                    print(Number, ":", f"Error checking Internal link:", {r.status_code, r.reason})
                    Number += 1
                    print(f"------------------------------")

            print(f"*************************************")
            print(f"...Links Check Completed...")










