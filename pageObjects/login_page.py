from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Tests import readCreds


class loginPage:
    __url = "https://digitalbriefcase.alkermes.info/"
    __username_textField = (By.ID, 'username')
    __password_textField = (By.ID, 'pwd')
    __login_button = (By.XPATH, "//span[normalize-space()='Sign In']")

    __goBtn = (By.ID, "go-btn")

    __Vivitrol_IDN = (By.XPATH, "//body[1]/app-root[1]/div[1]/dbc-blank-layout[1]/div[1]/dbc-product-selection[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/label[1]")
    __Vivitrol_CJ = (By.XPATH, "//body[1]/app-root[1]/div[1]/dbc-blank-layout[1]/div[1]/dbc-product-selection[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/label[1]")
    __Vivitrol_NTS = (By.XPATH, "//body[1]/app-root[1]/div[1]/dbc-blank-layout[1]/div[1]/dbc-product-selection[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[2]/div[2]/div[3]/div[3]/div[1]/label[1]")

    __Lybalvi_IDN = (By.XPATH, "//div[@class='text-center pt-40 w-100 product-layout']//div[2]//div[2]//div[1]//div[1]//div[1]//label[1]//span[1]")

    __Aristada_IDN = (By.XPATH, "//body[1]/app-root[1]/div[1]/dbc-blank-layout[1]/div[1]/dbc-product-selection[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[4]/div[2]/div[1]/div[1]/div[1]/label[1]")
    __Aristada_CJ = (By.XPATH, "//body[1]/app-root[1]/div[1]/dbc-blank-layout[1]/div[1]/dbc-product-selection[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[4]/div[2]/div[2]/div[2]/div[1]/label[1]")

    __treatment = (By.XPATH, "(//div[@class='resources-icon'])[3]")
    __all_links = (By.TAG_NAME, "a")
    __aristadaCheckboxOne = (By.XPATH, "//body[1]/app-root[1]/div[1]/dbc-blank-layout[1]/div[1]/dbc-product-selection[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[4]/div[2]/div[1]/div[1]/div[1]/label[1]/span[1]")
    __eye = (By.XPATH, "//body[1]/app-root[1]/div[1]/dbc-basic-layout[1]/main[1]/dbc-resources[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/mat-tab-group[1]/div[1]/mat-tab-body[1]/div[1]/div[1]/div[1]/div[1]/div[23]/div[1]/div[2]/div[1]/span[1]")
    __branded = (By.XPATH, "//div[@id='mat-tab-label-22-1']//div[@class='mat-tab-label-content'][normalize-space()='BRANDED']")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(self.__url)

    @property
    def current_url(self):
        return self._driver.current_url

    def perform_Kamlogin(self):
        pass_username = self._driver.find_element(*self.__username_textField)
        pass_password = self._driver.find_element(*self.__password_textField)
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__login_button))
        press_loginBtn = self._driver.find_element(*self.__login_button)
        username = readCreds.read_data(2, 1)
        password = readCreds.read_data(2, 2)
        pass_username.send_keys(username)
        pass_password.send_keys(password)
        press_loginBtn.click()


    def perform_mmdlogin(self):
        pass_username = self._driver.find_element(*self.__username_textField)
        pass_password = self._driver.find_element(*self.__password_textField)
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__login_button))
        press_loginBtn = self._driver.find_element(*self.__login_button)
        username = readCreds.read_data(3, 1)
        password = readCreds.read_data(3, 2)
        pass_username.send_keys(username)
        pass_password.send_keys(password)
        press_loginBtn.click()

    def perform_tradelogin(self):
        pass_username = self._driver.find_element(*self.__username_textField)
        pass_password = self._driver.find_element(*self.__password_textField)
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__login_button))
        press_loginBtn = self._driver.find_element(*self.__login_button)
        username = readCreds.read_data(4, 1)
        password = readCreds.read_data(4, 2)
        pass_username.send_keys(username)
        pass_password.send_keys(password)
        press_loginBtn.click()

    def click_goBtn(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__goBtn))
        self._driver.find_element(*self.__goBtn).click()


    def click_Vivitrol_IDN(self):
        wait = WebDriverWait(self._driver, 20)
        wait.until(ec.presence_of_element_located(self.__Vivitrol_IDN))
        self._driver.find_element(*self.__Vivitrol_IDN).click()

    def click_Vivitrol_CJ(self):
        wait = WebDriverWait(self._driver, 20)
        wait.until(ec.presence_of_element_located(self.__Vivitrol_CJ))
        self._driver.find_element(*self.__Vivitrol_CJ).click()

    def click_Vivitrol_NTS(self):
        wait = WebDriverWait(self._driver, 20)
        wait.until(ec.presence_of_element_located(self.__Vivitrol_NTS))
        self._driver.find_element(*self.__Vivitrol_NTS).click()

    def click_Lybalvi_IDN(self):
        wait = WebDriverWait(self._driver, 20)
        wait.until(ec.presence_of_element_located(self.__Lybalvi_IDN))
        self._driver.find_element(*self.__Lybalvi_IDN).click()

    def click_Aristada_IDN(self):
        wait = WebDriverWait(self._driver, 20)
        wait.until(ec.presence_of_element_located(self.__Aristada_IDN))
        self._driver.find_element(*self.__Aristada_IDN).click()

    def click__Aristada_CJ(self):
        wait = WebDriverWait(self._driver, 20)
        wait.until(ec.presence_of_element_located(self.__Aristada_CJ))
        self._driver.find_element(*self.__Aristada_CJ).click()






