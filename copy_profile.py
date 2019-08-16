from selenium import webdriver
from time import sleep
import requests
import argparse
import sys


parser = argparse.ArgumentParser(description="Instagram Photo Downloader")
parser.add_argument('-u', '--username', action='store', dest='username', help='Username of profile to download from')
parser.add_argument('-p', '--password', action='store', dest='password', help='Password of profile to download from')
parser.add_argument('-d', '--destination', action='store', dest='destination', help='Destination folder to store files')
args = parser.parse_args()


# need a delay else instagram will flag as suspicious
def send_keys_with_delay(element, text):
    for char in text:
        element.send_keys(char)
        sleep(0.33)

def navigate_to_private_profile(driver):
	print("Navigating to profile...")
	driver.get("https://www.instagram.com")
	driver.find_element_by_link_text("Log in").click()
	sleep(3)
	username_field = driver.find_element_by_name("username")
	send_keys_with_delay(username_field, username)
	sleep(3)
	password_field = driver.find_element_by_name("password")
	send_keys_with_delay(password_field, password)
	sleep(3)
	driver.find_element_by_xpath("//div[contains(text(), 'Log')]").click()
	sleep(3)
	driver.find_element_by_xpath("//button[text()='Not Now']").click()
	sleep(3)
	driver.find_element_by_xpath("//span[@aria-label='Profile']").click()


def navigate_to_public_profile(driver):
	print("Navigating to profile")
	driver.get("https://instagram.com/" + username)


def collect_images(destination):
	print("Collecting images...")
	pictures = driver.find_elements_by_tag_name("img")
	i = 0
	for picture in pictures:
		src = picture.get_attribute("src")
		resp = requests.get(src)
		if resp.status_code == 200:
			name_of_file = destination + 'picture_' + str(i) + '.jpg'
			with open(name_of_file, 'wb') as f:
				f.write(resp.content)


username = args.username
password = args.password
destination = args.destination

if not destination:
	destination = '.'
if not username:
	print("Please provide a username")
	driver.close()
	sys.exit()
if not password:
	driver = webdriver.Chrome()
	navigate_to_public_profile(driver)
else:
	driver = webdriver.Chrome()
	navigate_to_private_profile(driver)

collect_images(destination)
driver.close()


