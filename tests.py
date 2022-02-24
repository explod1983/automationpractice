from pathlib import Path
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Lib.home_page import HomePage
from Lib.user_registration import UserReg
from Lib.product_item import ProductItem
from Lib.payment_process import PaymentProcess

chrome_path = Path(__file__).parent.absolute() / 'chromedriver_win32\chromedriver.exe'
service = Service(str(chrome_path))
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


class PurchaseScenarios(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=service, options=options)
        self.home_p = HomePage(self.browser)
        self.user_reg = UserReg(self.browser)
        self.product_item = ProductItem(self.browser)
        self.payment_p = PaymentProcess(self.browser)

    def tearDown(self) -> None:
        self.addCleanup(self.browser.quit)

    def test_purchase_one_product_three_items(self) -> None:
        """
        Use case:
        Not registered user select one product -> appears on a product detailed page ->
        -> Add quantity -> Proceed to check out -> Check the cart items and price-> Proceed to check out ->
        -> Create an account -> Proceed to check out -> Address -> Shipment -> Payment ->
        -> Verify successful payment
        """
        self.home_p.open_home_page()
        self.home_p.open_first_product_in_the_list()
        self.product_item.add_quantity_with_plus_button(quantity=3)
        self.product_item.add_to_cart()
        self.product_item.proceed_to_checkout()

        # Check item total price calculation:
        item_price = float(str(self.payment_p.item_price()).replace('$', ''))
        item_quantity = int(self.payment_p.get_unit_quantity())
        total_item_price = float(str(self.payment_p.one_item_total_price()).replace('$', ''))
        self.assertEqual(item_price * item_quantity, total_item_price)

        # Check cart total price calculation without tax:
        total_items_in_cart_price = float(str(self.payment_p.total_products_price()).replace('$', ''))
        shipping_price = float(str(self.payment_p.total_shipping_price()).replace('$', ''))
        total_price_without_tax = float(str(self.payment_p.total_price_without_tax()).replace('$', ''))
        self.assertEqual(total_items_in_cart_price + shipping_price, total_price_without_tax)

        # Check cart total price calculation with tax:
        tax_price = float(str(self.payment_p.tax()).replace('$', ''))
        total_cart_price = float(str(self.payment_p.total_cart_price()).replace('$', ''))
        self.assertEqual(total_price_without_tax + tax_price, total_cart_price)
        self.payment_p.proceed_checkout()

        # Create account:
        self.user_reg.create_account_with_random_email()
        self.user_reg.enter_personal_information()
        self.user_reg.enter_your_address()

        # Address and shipping data:
        self.payment_p.address_proceed_to_checkout()
        self.payment_p.shipping_proceed_to_checkout()
        self.payment_p.pay_by_check()
        self.payment_p.confirm_order()

        # Check success alert message:
        self.assertEqual(self.payment_p.check_succes_alert(), 'Your order on My Store is complete.')

        # Check total amount on confirmation page:
        self.assertEqual(float(str(self.payment_p.check_total_price()).replace('$', '')), total_cart_price)


if __name__ == '__main__':
    unittest.main()
