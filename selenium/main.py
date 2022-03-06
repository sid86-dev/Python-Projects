from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
search = driver.find_element_by_xpath('//*[@id="search"]')
search.send_keys('Throttlerz')


btn = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
btn.click()