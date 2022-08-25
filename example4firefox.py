# selenium 4
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver4FirefoxBrowser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver4FirefoxBrowser.get('http://www.google.com')
time.sleep(15) #seconds
assert 'Google' in driver4FirefoxBrowser.title
driver4FirefoxBrowser.close()