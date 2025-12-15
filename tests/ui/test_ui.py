import pytest
import json
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# Cargar datos desde JSON
with open('datos/test_data.json') as f:
    test_data = json.load(f)

class TestUI:
    
    def test_login_exitoso(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        
        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        
        assert inventory_page.get_title() == "Products"

    @pytest.mark.parametrize("datos", test_data)
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
        inventory_page.go_to_cart()
        
        assert "cart.html" in driver.current_url

    def test_fallido_intencional(self, driver):
        driver.get("https://www.saucedemo.com/")
        assert driver.title == "Titulo Incorrecto"