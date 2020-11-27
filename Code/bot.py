
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
import os
import time
import getpass
import logging
import traceback
import datetime
import re
import glob
import json
import sys


def bot_run():


	file_folder=(f"{os.path.dirname(os.path.realpath(__file__))}")
	options = webdriver.ChromeOptions() #calling webdriver 
	options.add_argument('--ignore-vertificate-errors') #tells chrome driver what to do as ignore certificate error and ssl errors
	# options.add_argument("--headless")
	options.add_argument('--ignore-ssl-errors') # ignores ssl certificates
	options.add_argument("--incognito") #incognito mode for a clean browser with no add-ons
	options.add_argument("--start-maximized") # maximizes browser window
	chromedriver = f'{file_folder}\\chromedriver.exe' #concatenation that adds path
	os.environ["webdriver.chrome.driver"] = chromedriver #telling os what kind of browser using from selenium
	# chrome browser opens
	driver = webdriver.Chrome(chrome_options = options, executable_path = chromedriver) # defines webdriver and passes parameters. telling driver where chrome driver files are located
	# driver.close()
	driver.get("https://www.google.com")
	
    






if __name__ == "__main__":
    bot_run()