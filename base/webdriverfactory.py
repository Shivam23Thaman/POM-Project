from selenium import webdriver
import traceback

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseURL = "https://courses.letskodeit.com/"
        
        # opt = webdriver.ChromeOptions()
        # opt.add_argument("user-data-dir=/home/shivam/.config/google-chrome/Default")
        
        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        else:
            #driver = webdriver.Chrome(options=opt)
            driver = webdriver.Chrome()

        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(baseURL)

        return driver

