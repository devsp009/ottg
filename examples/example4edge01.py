import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver4EdgeBrowser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver4EdgeBrowser.get('https://microsoft.com')

time.sleep(15) #seconds
assert 'Google' in driver4EdgeBrowser.title
driver4EdgeBrowser.close()