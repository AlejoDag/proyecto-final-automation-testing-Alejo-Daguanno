import pytest
import json
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))

json_path = os.path.join(project_root, 'datos', 'test_data.json')

with open(json_path) as f:
    test_data = json.load(f)


class TestUI:
    
    def test_login_exitoso(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        
        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        
        assert inventory_page.get_title() == "Products"

    @pytest.mark.parametrize("data", test_data)
    def test_login_data_driven(self, driver, data):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        
        driver.get("https://www.saucedemo.com/")
        login_page.login(data["user"], data["pass"])

        if data["type"] == "valid":
            assert inventory_page.get_title() == "Products"
        else:
            assert "Epic sadface" in login_page.get_error_message()

    def test_agregar_carrito(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        
        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        inventory_page.add_backpack_to_cart()
        
        assert inventory_page.get_cart_count() == "1"

    def test_navegacion_carrito(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        
        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")

        inventory_page.add_backpack_to_cart()

        assert inventory_page.get_cart_count() == "1"

        inventory_page.go_to_cart()

        WebDriverWait(driver, 10).until(EC.url_contains("cart.html"))
        assert "cart.html" in driver.current_url

    def test_fallido_intencional(self, driver):
        driver.get("https://www.saucedemo.com/")
        assert driver.title == "Titulo Incorrecto"
