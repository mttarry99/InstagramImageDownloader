from selenium import webdriver
from time import sleep
import requests
import argparse
import sys
import os



def parse_args():
	parser = argparse.ArgumentParser(description="Instagram Photo Downloader")
	parser.add_argument('-u', '--username', action='store', dest='username', help='Username of profile to download from')
	parser.add_argument('-p', '--password', action='store', dest='password', help='Password of profile to download from')
	parser.add_argument('-d', '--destination', action='store', dest='destination', help='Destination folder to store files')
	global args
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


def navigate_to_public_profile(username):
	print("Navigating to profile")
	driver.get("https://instagram.com/" + username)


def collect_images(destination, username):
	print("Collecting images...")
	os.mkdir(destination + '/InstagramPhotos_' + username)
	pictures = driver.find_elements_by_tag_name("img")
	i = 0
	for picture in pictures:
		src = picture.get_attribute("src")
		resp = requests.get(src)
		if resp.status_code == 200:
			name_of_file = destination + '/InstagramPhotos_' + username + '/picture_' + str(i) + '.jpg'
			with open(name_of_file, 'wb') as f:
				f.write(resp.content)


				
def main():
	parse_args()
	
	username = args.username
	password = args.password
	destination = args.destination

	if not destination:
		destination = os.getcwd()
	if not username:
		raise Exception('Please provide a username')
		sys.exit()

	global driver
	driver = webdriver.Chrome()

	if not password:
		navigate_to_public_profile(username)
	else:
		navigate_to_private_profile(username)

	collect_images(destination, username)
	driver.quit()
	
if __name__ == "__main__":
	main()


