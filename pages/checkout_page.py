from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    CHECKOUT_BTN = (By.ID, "checkout")

    FIRST_NAME = (By.CSS_SELECTOR, "[data-test='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "[data-test='lastName']")
    ZIP_CODE = (By.CSS_SELECTOR, "[data-test='postalCode']")

    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")

    SUCCESS_HEADER = (By.CLASS_NAME, "complete-header")

    def click_checkout(self):
        self.force_click(self.CHECKOUT_BTN)

    def fill_information(self, first, last, zip_code):
        self.send_keys(self.FIRST_NAME, first)
        self.send_keys(self.LAST_NAME, last)
        self.send_keys(self.ZIP_CODE, zip_code)

    def click_continue(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTINUE_BTN)
        )
        btn.click()

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("checkout-step-two.html")
        )

    def click_finish(self):
        self.force_click(self.FINISH_BTN)

    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SUCCESS_HEADER)
        ).text

