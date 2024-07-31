from selenium.webdriver.common.by import By

class Job_search_locators():
    SEARCH_BOX = (By.NAME, "q")
    LOCATION_BOX = (By.NAME, "l")
    SEARCH_BTN = (By.XPATH, "//button[@type='submit']")
    #QUICK_APPLY = (By.XPATH, "//div[@class = 'css-2imjyh']//p[@class = 'chakra-text css-u40boz'][normalize-space()='Quick apply']")
    JOBS_LISTS = (By.XPATH, "//div[@class = 'css-17iqsqz']")
    JOBS_TITLE_LISTS =  "//a[@class = 'chakra-button css-1djbb1k']"
    JOB_POSTED_TIME =  "//div[@class = 'css-17iqsqz']//p[@class = 'chakra-text css-5yilgw']"
    DATE_FILTER = (By.XPATH, "//button[@id='menu-button-:rp:']")
    DATE_24H = (By.XPATH, "//button[@id='menu-list-:rp:-menuitem-:r4n:']//span[contains(text(),'24 hours')]")

    @staticmethod
    def get_job_title_xpath(job_title):
        return f"//a[normalize-space(text())='{job_title}']"

class Job_apply_locators():
    QUICK_APPLY = (By.XPATH, "//a[@class='chakra-button css-24yw96'][normalize-space()='Quick apply']")
    APPLY_NOW = (By.XPATH, "//a[@class='chakra-button css-1wzc2gy'][normalize-space()='Apply Now']")
    SIGN_IN_POPUP = (By.XPATH, "//div[@class='chakra-modal__body css-8gwcja']")

class SigninPage_locators():
    SIGNIN_BUTTON = (By.XPATH, "//button[@class='chakra-button css-1l9fvt3'][normalize-space()='Sign In or Sign Up']")
    USERNAME_EMAIL = (By.ID, "ifl-InputFormField-ihl-useId-passport-webapp-1")
    #USERNAME_CONTINUE = (By.CLASS_NAME, "dd-privacy-allow css-1u4g79g e8ju0x50")
    NEXTPAGE_CONTINUE = (By.XPATH, "//*[@id='googleContainer']/button")
    IDENTIFIERID = (By.ID, "identifierId")
    PW_FIELD = (By.CLASS_NAME, "whsOnd zHQkBf")
    SUCCESS = (By.ID, "chakra-modal--body-:Rfqlal6j6lbbaqld9fbqm:")

