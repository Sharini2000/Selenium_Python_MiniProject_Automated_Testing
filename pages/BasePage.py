import openpyxl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def wait_for_element(self, *locator, timeout=20):
        """Wait for the element identified by the locator to be present on the page."""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, *locator, timeout=20):
        """Wait for the element identified by the locator to be clickable."""
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))