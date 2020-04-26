
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOTS = os.path.join(BASE_DIR, 'screenshots')
OUTPUT = os.path.join(BASE_DIR, 'output')

if not os.path.exists(SCREENSHOTS):
	os.mkdir(SCREENSHOTS)
if not os.path.exists(OUTPUT):
	os.mkdir(OUTPUT)

def initiate_webdirver(headless=True):

	desired_capabilities = DesiredCapabilities.CHROME.copy()
	options = webdriver.ChromeOptions()

	if headless:
		options.add_argument('--headless')

	## Below setting to automatically download files from the chrome browser to specified path
	options.add_experimental_option("prefs", {
	      "download.default_directory": r'{}'.format(SCREENSHOTS),  # download file_path
	      "download.prompt_for_download": False,
	      "download.directory_upgrade": True,
	      "safebrowsing.enabled": False,
	      "safebrowsing.disable_download_protection": True,
	    })
	desired_capabilities = options.to_capabilities()

	driver = webdriver.Chrome(desired_capabilities=desired_capabilities)

	return driver
