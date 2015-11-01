from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import base64

import time


# some browser settings


def hin2eng(text):

	fp = webdriver.FirefoxProfile()
	driver = webdriver.Firefox(firefox_profile=fp)
	driver.get("http://translate.google.com")


	# global driver

	driver.get("https://translate.google.com/#auto/en")
	driver.find_element_by_css_selector("#source").click()
	driver.find_element_by_css_selector("#source").send_keys(text)

	driver.find_element_by_css_selector("#gt-submit").click()

	result = ""

	while  result.strip() == "":
		result = driver.find_element_by_css_selector("#result_box").text
	print result


def eng2hin(text):

	fp = webdriver.FirefoxProfile()
	driver = webdriver.Firefox(firefox_profile=fp)
	driver.get("http://translate.google.com")


	driver.get("https://translate.google.com/#auto/hi")

	driver.find_element_by_css_selector("#source").click()
	driver.find_element_by_css_selector("#source").send_keys(text)

	driver.find_element_by_css_selector("#gt-submit").click()

	result = ""

	while  result.strip() == "":
		result = driver.find_element_by_css_selector("#result_box").text

	print result



