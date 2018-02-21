from selenium import webdriver
import time

browser = webdriver.PhantomJS()
browser.get('http://localhost:7001/')
browser.save_screenshot("images/"+"_".join(str(time.time()).split("."))+'.png')
browser.quit()
