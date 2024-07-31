import time
import pandas as pd
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from utils.locators import Job_apply_locators as JAL
from utils.screenshot import ScreenshotHelper
from pages.BasePage import BasePage
from utils.locators import Job_search_locators as JL
from pages.pages_job_search import Job_Search_Page as JSP
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

screenshot_helper = ScreenshotHelper()

class Job_Apply_Page(BasePage):

    def __init__(self, driver, job_title, username, password):
        super().__init__(driver)
        self.driver = driver
        self.job_title = job_title
        self.username = username
        self.password = password


    def job_apply(self):
        job_search_obj = JSP(self.driver, self.job_title, self.username, self.password)
        search_box = self.wait_for_element(*JL.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(self.job_title)
        time.sleep(5)
        location_box = self.wait_for_element(*JL.LOCATION_BOX)
        location_box.send_keys(Keys.CONTROL + 'a')
        location_box.send_keys(Keys.BACKSPACE)
        location_box.send_keys("Canada")
        location_box.send_keys(Keys.ENTER)
        time.sleep(5)
        search_btn = self.driver.find_element(*JL.SEARCH_BTN)
        time.sleep(5)
        search_btn.click()
        job_search_obj.select_job()
        try:
            quick_apply = self.wait_for_element(*JAL.QUICK_APPLY)
            if quick_apply:
                quick_apply.click()
        except NoSuchElementException:
            try:
                apply_now = self.wait_for_element(*JAL.APPLY_NOW)
                if apply_now:
                    apply_now.click()
            except NoSuchElementException:
                print("Neither 'Quick apply' nor 'Apply now' button found.")

        time.sleep(3)
        screenshot_helper.take_screenshot(self.driver, "Job_Apply_Button_Click_Results")

        singin_popup = self.wait_for_element(*JAL.SIGN_IN_POPUP)
        if singin_popup:
            screenshot_helper.take_screenshot(self.driver, "SingIn/SingUp Popup appears")
            return True
        else:
            return False





