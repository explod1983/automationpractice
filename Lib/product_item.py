from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class ProductItem:

    def __init__(self, browser):
        self.browser = browser

    def add_quantity_with_plus_button(self, quantity):
        for _ in range(quantity):
            self.browser.find_element(By.XPATH, '//*[@id="quantity_wanted_p"]/a[2]/span/i').click()

    def add_to_cart(self):
        return self.browser.find_element(By.CSS_SELECTOR, 'button.exclusive').click()

    def proceed_to_checkout(self):
        return wait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, ".//a[contains(@title,'Proceed to checkout')]"))).click()

