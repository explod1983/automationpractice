from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def open_home_page(self):
        return self.browser.get('http://automationpractice.com/')

    def open_first_product_in_the_list(self):
        return wait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, ".//a[contains(@title,'Faded Short Sleeve T-shirts')]"))).click()


