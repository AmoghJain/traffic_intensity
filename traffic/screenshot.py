from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:7000/')
browser.save_screenshot('screenie.png')
browser.quit()