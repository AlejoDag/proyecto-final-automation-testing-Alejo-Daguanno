from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest 
from utils.datos import leer_csv_login
from pages.login_page import LoginPage


@pytest.mark.parametrize("usuario,password,debe_funcionar",leer_csv_login("datos/data_login.csv"))
def test_login_validation(login_in_driver,usuario,password,debe_funcionar):
    driver = login_in_driver
    print(debe_funcionar)
    if debe_funcionar:
        assert "/inventory.html" in driver.current_url, "No se redirgió al inventario"
    else:
        mensaje_error = LoginPage(driver).obtener_error()
        assert "Epic sadface" in mensaje_error, "el mensaje de error no se esta mostrando"

