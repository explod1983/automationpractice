from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from .static_data import User


class UserReg:

    def __init__(self, browser):
        self.browser = browser
        self.user = User()

    def create_account_with_random_email(self):
        wait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="email_create"]'))).send_keys(self.user.EMAIL)
        self.browser.find_element(By.XPATH, '//*[@id="SubmitCreate"]').click()

    def enter_personal_information(self):
        wait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="id_gender1"]'))).click()
        self.browser.find_element(By.XPATH, '//*[@id="customer_firstname"]').send_keys(self.user.NAME)
        self.browser.find_element(By.XPATH, '//*[@id="customer_lastname"]').send_keys(self.user.LASTNAME)
        self.browser.find_element(By.XPATH, '//*[@id="email"]').click()
        self.browser.find_element(By.XPATH, '//*[@id="passwd"]').send_keys(self.user.PASSWORD)

    def enter_your_address(self):
        self.browser.find_element(By.XPATH, '//*[@id="firstname"]').send_keys(self.user.NAME)
        self.browser.find_element(By.XPATH, '//*[@id="lastname"]').send_keys(self.user.LASTNAME)
        self.browser.find_element(By.XPATH, '//*[@id="address1"]').send_keys(self.user.ADDRESS)
        self.browser.find_element(By.XPATH, '//*[@id="city"]').send_keys(self.user.CITY)
        Select(self.browser.find_element(By.XPATH, '//*[@id="id_state"]')).select_by_value('5')
        self.browser.find_element(By.XPATH, '//*[@id="postcode"]').send_keys(self.user.ZIP_CODE)
        Select(self.browser.find_element(By.XPATH, '//*[@id="id_country"]')).select_by_value('21')
        self.browser.find_element(By.XPATH, '//*[@id="phone_mobile"]').send_keys(self.user.PHONE)
        self.browser.find_element(By.XPATH, '//*[@id="alias"]').click()
        self.browser.find_element(By.XPATH, '// *[ @ id = "submitAccount"]').click()
