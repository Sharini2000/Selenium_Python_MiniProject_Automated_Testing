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
from utils.locators import SigninPage_locators as SPL

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

screenshot_helper = ScreenshotHelper()


class SignIn(BasePage):
    def __init__(self, driver, job_title, username, password):
        super().__init__(driver)
        self.driver = driver
        self.job_title = job_title
        self.username = username
        self.password = password


    def SignIn_Process(self):
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
        screenshot_helper.take_screenshot(self.driver, "SignIn Popup")
        signin_button = self.wait_for_element(*SPL.SIGNIN_BUTTON)
        signin_button.click()
        parent_win = self.driver.current_window_handle
        all_win = self.driver.window_handles
        for win in all_win:
            if win != parent_win:
                self.driver.switch_to.window(win)
        screenshot_helper.take_screenshot(self.driver, "Username Field")
        signin_success = self.username_password_entries()
        return signin_success


    def username_password_entries(self):
        username_field = self.wait_for_element(*SPL.USERNAME_EMAIL)
        username_field.send_keys(self.username)
        time.sleep(3)
        screenshot_helper.take_screenshot(self.driver, "Username_Entry")
        # username_continue = self.wait_for_element(*SPL.USERNAME_CONTINUE)
        # username_continue.click()
        continue_email = self.wait_for_element(*SPL.NEXTPAGE_CONTINUE)
        continue_email.click()
        parent_win1 = self.driver.current_window_handle
        all_win1 = self.driver.window_handles
        for win1 in all_win1:
            if win1 != parent_win1:
                self.driver.switch_to.window(win1)

        identierid = self.wait_for_element(*SPL.IDENTIFIERID)
        identierid.clear()
        identierid.send_keys(self.username)
        time.sleep(3)
        identierid.send_keys(Keys.ENTER)
        password_field = self.wait_for_element(*SPL.PW_FIELD)
        password_field.clear()
        password_field.send_keys(self.password)
        time.sleep(3)
        screenshot_helper.take_screenshot(self.driver, "Password_Entry")
        password_field.send_keys(Keys.ENTER)
        success = self.wait_for_element(*SPL.SUCCESS)
        time.sleep(3)
        if success:
            screenshot_helper.take_screenshot(self.driver, "SignIn Success PopUp")
            return True
        else:
            screenshot_helper.take_screenshot(self.driver, "SignIn Unsuccessful PopUp")
            return False








