import pytest
import json
import os
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.support.ui import WebDriverWait


# Carga de datos de prueba
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
json_path = os.path.join(project_root, 'datos', 'test_data.json')

with open(json_path) as f:
    test_data = json.load(f)

class TestUI:

    def test_1_login_exitoso(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        assert inventory_page.get_title() == "Products"

    def test_2_login_invalido(self, driver):
        login_page = LoginPage(driver)
        driver.get("https://www.saucedemo.com/")
        login_page.login("usuario_falso", "clave_falsa")
        assert "Epic sadface" in login_page.get_error_message()

    def test_3_agregar_carrito(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        
        inventory_page.add_backpack_to_cart()
        assert inventory_page.get_cart_count() == "1"

    def test_4_filtro_precio(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")

        inventory_page.sort_by_price_low_to_high()

        assert "$7.99" in inventory_page.get_first_item_price()

    def test_5_checkout_completo(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        checkout_page = CheckoutPage(driver)

        # 1. Login y agregar al carrito
        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        inventory_page.add_backpack_to_cart()
        inventory_page.go_to_cart()
        
        # 2. Iniciar Checkout
        checkout_page.click_checkout()
        
        # 3. Llenar formulario de información
        checkout_page.fill_information("Juan", "Perez", "1234")

        # 4. PASO CRUCIAL: Ir a la siguiente página (Overview)
        checkout_page.click_continue()

        # 5. Finalizar la compra
        checkout_page.click_finish()
        
        # 6. Validar mensaje de éxito
        mensaje = WebDriverWait(driver, 10).until(
            lambda d: checkout_page.get_success_message()
        )   
        assert "Thank you for your order!" in mensaje
