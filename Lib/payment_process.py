from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class PaymentProcess:

    def __init__(self, browser):
        self.browser = browser

    def item_price(self):
        return wait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#cart_summary tbody td.cart_unit .price span"))).text

    def get_unit_quantity(self):
        elem = self.browser.find_element(By.CSS_SELECTOR, ".cart_quantity .cart_quantity_input")
        return elem.get_attribute("value")

    def one_item_total_price(self):
        return self.browser.find_element(By.CSS_SELECTOR, "td.cart_total").text

    def total_products_price(self):
        return self.browser.find_element(By.CSS_SELECTOR, "#total_product").text

    def total_shipping_price(self):
        return self.browser.find_element(By.CSS_SELECTOR, "#total_shipping").text

    def total_price_without_tax(self):
        return self.browser.find_element(By.CSS_SELECTOR, "#total_price_without_tax").text

    def tax(self):
        return self.browser.find_element(By.CSS_SELECTOR, "#total_tax").text

    def total_cart_price(self):
        return self.browser.find_element(By.CSS_SELECTOR, "#total_price").text

    def proceed_checkout(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".standard-checkout > span").click()

    def address_proceed_to_checkout(self):
        wait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.button:nth-child(4)'))).click()

    def shipping_proceed_to_checkout(self):
        self.browser.find_element(By.XPATH, '// *[ @ id = "uniform-cgv"]').click()
        self.browser.find_element(By.CSS_SELECTOR, 'button.button:nth-child(4)').click()

    def pay_by_check(self):
        self.browser.find_element(By.XPATH, ".//a[contains(@title,'Pay by check.')]").click()

    def confirm_order(self):
        self.browser.find_element(By.CSS_SELECTOR, 'button.button-medium').click()

    def check_succes_alert(self):
        return self.browser.find_element(By.CSS_SELECTOR, '.alert').text

    def check_total_price(self):
        return self.browser.find_element(By.CSS_SELECTOR, 'span.price:nth-child(2)').text