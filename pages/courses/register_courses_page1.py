import sys 
sys.path.append("/home/shivam/Documents/selenium_novice_project")
from base.basepage import BasePage
from selenium.webdriver.common.keys import Keys 
import utilities.custom_logger as cl
import logging
from selenium.webdriver.support.select import Select
from selenium import webdriver
import time 

class RegisterCoursesPage(BasePage):
	log = cl.customLogger(logging.DEBUG)

	def __init__(self, driver):
		super().__init__(driver)
		self.driver = driver

	# LOCATORS

	search_box = "input[name='course']" # css
	all_courses = "ALL COURSES" #LINK
	course_locator = "//h4[contains(text(), '{0}')]" # xpath
	enroll_button = "//button[text()= 'Enroll in Course']" # xpath
	order_summary_block = "checkout-order-summary" # id
	contact_email_field = "input[placeholder='Email Address']"
	Already_have_an_account = "//p[contains(text(), 'Already have an account')]" # xpath
	contact_login_link = "a[title='Already have an account?']" # css
	email_required = "//div[contains(@class,'email')]//span[text() = 'This field is required']"
	cc_block = "div.stripe-outer"
	iframe = "iframe[title*='{0}']" #css
	cc_number = "input[placeholder= 'Card Number']" # css
	cc_exp  = "exp-date" # name
	cc_cvv = 'cvc' # name
	country = "country-list" # name
	#sel = Select(country)
	#country_locator = sel.select_by_visible_text({0})
	submit_enroll = "//button[contains(@class, 'sp-buy')]" # xpath

	cc_error_message = '''//li[contains(@class, 'text-danger')]
	//span[contains(text(), '{0}')]'''

	logout_contact_info = "//a[text() = 'Logout' and @role='button']" # xpath

	def enterCourseName(self, searchterm):
		try:
			course = self.sendKeys(searchterm, self.search_box, 'css')
			self.sendKeys(Keys.ENTER, self.search_box, 'css') 
		except:
			self.log.error("Exception Occured!! Could not search or press Enter key on search")

	open_course = lambda self, fullname: self.elementClick(self.course_locator.format(fullname), 
		locatorType="xpath")

	click_enroll_button = lambda self: self.elementClick(self.enroll_button, 
		locatorType='xpath')

	get_iframe = lambda self, value : self.getElement(self.iframe.format(value), 'css')

	#enterCardNum = lambda self, num: self.sendKeys(num, self.cc_number, locatorType='css')
	def enterCardNum(self, num):
		self.switchToFrame(title=self.get_iframe('card number'))
		self.sendKeys(num, self.cc_number, locatorType='css')
		self.switchToDefaultContent()

	def enterCardExp(self, exp):
		self.switchToFrame(title=self.get_iframe('expiration date'))
		self.sendKeys(exp, locator=self.cc_exp, locatorType="name")
		self.switchToDefaultContent()

	def enterCardCVV(self, cvv):
		self.switchToFrame(title=self.get_iframe("CVC"))
		self.sendKeys(cvv, locator=self.cc_cvv, locatorType="name")
		self.switchToDefaultContent()


	clickEnrollSubmitButton = lambda self: self.elementClick(self.submit_enroll, 'xpath')

	def enterCreditCardInformation(self, num, exp, cvv):
		
		self.enterCardNum(num)
		self.enterCardExp(exp)
		self.enterCardCVV(cvv)


	def buyCourse(self, num='', exp='', cvv=''):
		#self.click_enroll_button()
		#self.webScroll(direction='down')
		credit_card_block = self.getElement(self.cc_block, 'css') 
		location = credit_card_block.location_once_scrolled_into_view
		self.waitForElement(self.cc_number, locatorType='xpath')
		self.enterCreditCardInformation(num, exp, cvv)
		self.clickEnrollSubmitButton()
	
	def clearCardNum(self):
		self.switchToFrame(title=self.get_iframe('card number'))
		self.clearField(self.cc_number, locatorType='css')
		self.switchToDefaultContent()

	def clearCardExp(self):
		self.switchToFrame(title=self.get_iframe('expiration date'))
		self.clearField(locator=self.cc_exp, locatorType="name")
		self.switchToDefaultContent()

	def clearCardCVV(self):
		self.switchToFrame(title=self.get_iframe("CVC"))
		self.clearField(locator=self.cc_cvv, locatorType="name")
		self.switchToDefaultContent()

	def clearCardFields(self):
		self.clearCardNum()
		self.clearCardExp()
		self.clearCardCVV()
		

	def verify_order_contact_payment_block_exists(self):
		result = self.isElementPresent("//h3[contains(text(), 'Payment Information')]", locatorType= 'xpath')
		return result
		

	def verifyEnrollSuccessful(self):
		pass

	def verifyErrorMsgDisp(self):
		error_messages = ['card number is incomplete', 'card number is invalid',
		'expiration date is incomplete', 'expiration year is in the past', 
		'expiration year is invalid','security code is incomplete']

		#resultlist = []

		for msg in error_messages:
			message_path = self.cc_error_message.format(msg)
			self.waitForElement(message_path)
			try:
				error_disp = self.isElementDisplayed(message_path, locatorType='xpath')
				if error_disp:
					#resultlist.append(msg)
					self.screenShot("error displayed")
					return error_disp

			except ValueError:
				self.log.error("Could not fill the Card values. Check if elements are out view.")
		#self.log.info(resultlist)

	def verifyBuyButtonDisabledOnError(self):

		result = self.isEnabled(locator=self.submit_enroll, locatorType="xpath",
	                            info="Enroll Button")
		return not result

	logout_contact_info_link = lambda self: self.elementClick(self.logout_contact_info, locatorType='xpath')

	def verify_logout(self):
		result = self.isElementDisplayed(self.Already_have_an_account, 'xpath') and self.isElementDisplayed(self.contact_login_link, 'css')
		
		return result 


		














	  

	
		










