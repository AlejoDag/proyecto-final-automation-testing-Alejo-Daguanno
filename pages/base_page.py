from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger()

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def click(self, locator):
        try:
            element = self.find_element(locator)
            element.click()
            self.logger.info(f"Click realizado en: {locator}")
        except Exception as e:
            self.logger.error(f"Error al hacer click en {locator}: {e}")
            raise

    def send_keys(self, locator, text):
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
            self.logger.info(f"Texto ingresado en {locator}")
        except Exception as e:
            self.logger.error(f"Error al escribir en {locator}: {e}")
            raise

    def get_text(self, locator):
        return self.find_element(locator).text