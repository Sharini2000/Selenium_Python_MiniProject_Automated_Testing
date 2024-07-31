import time
import pandas as pd
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from utils.locators import Job_search_locators as JL
from utils.screenshot import ScreenshotHelper
from pages.BasePage import BasePage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


jobs_postings = []

screenshot_helper = ScreenshotHelper()
class Job_Search_Page(BasePage):

    def __init__(self, driver, job_title, username, password):
        super().__init__(driver)
        self.driver = driver
        self.job_title = job_title
        self.username = username
        self.password = password



    def enter_job_title(self):
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
        screenshot_helper.take_screenshot(self.driver, "job_search_results")
        time.sleep(5)
        jobs_list_count = self.jobs_count()
        return jobs_list_count

    def jobs_count(self):


        # Wait until job listings are present
        self.wait_for_element(By.ID, "job-list")

        jobs_lists = self.driver.find_elements(By.XPATH, './/div[@class = "css-f8dtpc"]')
        print(f"Number of jobs listings in the current page: {len(jobs_lists)} ")
        for job in jobs_lists:
             try:
                 title = job.find_element(By.XPATH, './/div[@class = "chakra-stack css-1igwmid"]').text
                 jobs_posts = {
                     'Job_Titles': title,
                 }
                 jobs_postings.append(jobs_posts)
             except Exception as e:
                 print(f"Error occurred: {e}")
                 continue

        df = pd.DataFrame(jobs_postings)
        # Save DataFrame to CSV
        df.to_csv('jobs.csv', index=False)
        return len(jobs_lists)

    def select_job(self):
        if jobs_postings:
            job_title1 = jobs_postings[1]['Job_Titles']
            job1_xpath = JL.get_job_title_xpath(job_title1)
            job1 = self.wait_for_element(By.XPATH, job1_xpath)
            job1.click()
            screenshot_helper.take_screenshot(self.driver, "Select_some_random_job")
            time.sleep(3)




















