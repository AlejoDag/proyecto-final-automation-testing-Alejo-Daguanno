from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    TITLE = (By.CSS_SELECTOR, ".title")
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BTN = (By.ID, "remove-sauce-labs-backpack")

    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge") 
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def get_title(self):
        return self.get_text(self.TITLE)

    def add_backpack_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)
        self.find_element(self.REMOVE_BTN)

    def get_cart_count(self):
        return self.get_text(self.CART_BADGE)
    
    def go_to_cart(self):
        self.force_click(self.CART_LINK)
