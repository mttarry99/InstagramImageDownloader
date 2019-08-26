# Instagram Image Downloader
- Tool for saving Instagram photos from a user profile into a local folder
- Does not save username or password
- Uses Selenium and Chrome driver

## Requirements
- Python 3
- Selenium
- Chrome Driver

## Steps to install
1. Download [Python 3.6](https://www.python.org/downloads/release/python-360/)
2. Install [pip](https://pip.pypa.io/en/stable/installing/)
3. Download source code from Github
	```
	git clone https://github.com/mttarry99/InstagramImageDownloader.git
	cd InstagramImageDownloader
	```
4. Install required Python modules
	-```pip install -r requirements.txt```
5. Download and install [Chrome Driver](https://chromedriver.chromium.org/downloads)

## Usage
- Use command line arguments to specify:
	- username (-u, --username)
	- password (-p, --password)
	- destination (-d, --destination)
	
- For public accounts, only a username is required
- For private accounts, both a username and password are required

### Example Usage
```
# For a private account
python instagram_downloader.py -u [USERNAME] -p [PASSWORD] -d [DESTINATION FOLDER]

# For a public account
python instagram_downloader.py -u [USERNAME]
```
	

