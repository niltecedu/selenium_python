import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome()
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
driver.quit()