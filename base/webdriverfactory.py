from selenium import webdriver
import traceback

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebdriverInstance(self):
        baseURL = "https://letskodeit.teachable.com/"
        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Chrome()

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseURL)

        return driver

