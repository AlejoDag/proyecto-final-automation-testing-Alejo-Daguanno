from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger()

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def click(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))
            element.click()
            self.logger.info(f"Click realizado en: {locator}")
        except Exception as e:
            self.logger.error(f"Error al hacer click en {locator}: {e}")
            raise

    def force_click(self, locator, time=10):
        """Hace clic usando JavaScript directo (útil para elementos difíciles/tapados)"""
        try:
            element = self.find_element(locator, time)
            self.driver.execute_script("arguments[0].click();", element)
            self.logger.info(f"Force Click (JS) realizado en: {locator}")
        except Exception as e:
            self.logger.error(f"Error al hacer force click en {locator}: {e}")
            raise

    def send_keys(self, locator, text, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            self.logger.info(f"Texto ingresado en {locator}")
        except Exception as e:
            self.logger.error(f"Error al escribir en {locator}: {e}")
            raise

    def get_text(self, locator):
        return self.find_element(locator).text

