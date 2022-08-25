import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver4ChromeBrowser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver4ChromeBrowser.get('http://www.google.com')
time.sleep(15) #seconds
assert 'Google' in driver4ChromeBrowser.title
driver4ChromeBrowser.close()