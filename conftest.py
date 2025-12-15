import pytest
import pytest_html
from selenium import webdriver
from datetime import datetime
import os
from utils.logger import get_logger

logger = get_logger()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            screenshot_name = f"reports/screenshot_{item.name}_{timestamp}.png"
            driver.save_screenshot(screenshot_name)
            if os.path.exists(screenshot_name):
                
                extras.append(pytest_html.extras.image(screenshot_name))
        report.extras = extras

@pytest.fixture(scope="function")
def driver():
    logger.info("Iniciando navegador Chrome")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    
    driver_instance = webdriver.Chrome(options=options)
    driver_instance.implicitly_wait(5)
    
    yield driver_instance
    
    logger.info("Cerrando navegador")
    driver_instance.quit()
