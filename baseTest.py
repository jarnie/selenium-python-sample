# -*- coding: utf-8 -*-
import unittest
import xmlrunner
import time
import os
import urllib3
import requests
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from sauceclient import SauceClient
from requests.auth import HTTPBasicAuth

class baseTest(unittest.TestCase):
    screenshot_path = "./results/screenshots/"
    testPassed = False
    hamburgerMenuVisible = False
    sampleTestName = "test_1_open_page"
    browserstack_username = os.environ['BROW_STACK_USERNAME']
    browserstack_access_key = os.environ['BROW_STACK_ACCESS_KEY']
    sauce_username = os.environ['SAUCE_USERNAME']
    sauce_access_key = os.environ['SAUCE_ACCESS_KEY']

    def setUpChrome(self):
        print "Test case start"
        chromedriver = "./drivers/mac/chrome/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        os.environ["PYTHONIOENCODING"] = "UTF-8"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("window-size=1920x1080")
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
        return self.driver

    def setUpFF(self):
        print "Test case start"
        geckodriver = "./drivers/mac/gecko/geckodriver"
        os.environ["webdriver.gecko.driver"] = geckodriver
        os.environ["PYTHONIOENCODING"] = "UTF-8"
        ff_options = webdriver.FirefoxOptions()
        ff_options.add_argument("--headless")
        ff_options.add_argument("window-size=1920x1080")
        ff_options.add_argument("--start-maximized")
        self.driver = webdriver.Firefox(executable_path=geckodriver, firefox_options=ff_options)
        return self.driver

    def setUpFFSauceLabs(self, test_name):
        print "Test case start"
        #username = os.environ['SAUCE_USERNAME']
        #access_key = os.environ['SAUCE_ACCESS_KEY']
        self.sauce_client = SauceClient(baseTest.sauce_username, baseTest.sauce_access_key)
        desired_cap = {
            'platform': "macOS 10.13",
            'browserName': "firefox",
            'version': "64.0",
            'screenResolution' : "1920x1440",
            'name' : baseTest.sampleTestName,
        }
        self.driver = webdriver.Remote(
        command_executor='https://{}:{}@ondemand.saucelabs.com/wd/hub'.format(baseTest.sauce_username, baseTest.sauce_access_key),
        desired_capabilities=desired_cap)
        return self.driver

    def setUpFFWindowsSauceLabs(self, test_name):
        print "Test case start"
        self.sauce_client = SauceClient(baseTest.sauce_username, baseTest.sauce_access_key)
        desired_cap = {
            'platform': "Windows 10",
            'browserName': "firefox",
            'version': "62.0",
            'screenResolution' : "1920x1080",
            'name' : baseTest.sampleTestName,
        }

        self.driver = webdriver.Remote(
        command_executor='https://{}:{}@ondemand.saucelabs.com/wd/hub'.format(baseTest.sauce_username, baseTest.sauce_access_key),
        desired_capabilities=desired_cap)
        return self.driver

    def setUpFFBrowserStack(self):
        print "Test case start"
        desired_caps = {
            'os' : 'Windows',
            'os_version' : '10',
            'browser' : 'Firefox',
            'browser_version' : '62.0',
            'resolution' : '1920x1080',
            'browserstack.local' : 'false',
            'browserstack.geckodriver' : '0.22.0',
            'browserstack.selenium_version' : '3.14.0'
        }
        self.driver = webdriver.Remote(
        command_executor='https://{}:{}@hub.browserstack.com/wd/hub'.format(baseTest.browserstack_username, baseTest.browserstack_access_key),
        desired_capabilities=desired_caps)
        return self.driver

    def setUpChromeBitbar(self):
        print "Test case start"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("window-size=1600x1200")
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        return self.driver

    def tearDown(self):
        global testPassed
        print "End of test"
        sauce_run = os.environ['SAUCE_TESTRUN']
        brows_run = os.environ['BROW_STACK_TESTRUN']
        if sauce_run == "true":
            try:
                self.sauce_client.jobs.update_job(self.driver.session_id, passed=baseTest.testPassed)
            #except Exception as e: print(e)
            except:
                print "send results to sauce error"
            baseTest.testPassed = False
        if brows_run == "true":
            try:
                current_id = self.driver.session_id
                print "session id:"
                print current_id

                url = "https://api.browserstack.com/automate/sessions/" + current_id + ".json"
                headers = {
                'Content-type': 'application/json',
                }

                if baseTest.testPassed is True:
                    data={'name': baseTest.sampleTestName,'status': 'passed','reason': 'test-passed'}
                if baseTest.testPassed is False:
                    data={'name': baseTest.sampleTestName,'status': 'failed','reason': 'test-failed'}
                response = requests.put(url, auth=HTTPBasicAuth(baseTest.browserstack_username, baseTest.browserstack_access_key), headers=headers, data=json.dumps(data))

                print response
                baseTest.testPassed = False
            except:
                print "send results to browserstack error"
        self.driver.quit()

    def take_screenshot(self, name=None):
        time.sleep(1)
        if name is None:
            name = str(int(time.time()*1000))
        print "Taking screenshot: '" + name + "'"
        self.driver.save_screenshot(self.screenshot_path + name + ".png")

    def checkMenuElement(self):
        #self.driver.implicitly_wait(5)
        if not baseTest.hamburgerMenuVisible:
            try:
                self.driver.find_element_by_css_selector("ul[class='menu navigation__main-menu'] a[href='/startups/']")
                print "side menu visible"
                baseTest.hamburgerMenuVisible = False
            except NoSuchElementException:
                print "side menu item 'Startups' not visible"
                baseTest.hamburgerMenuVisible = True
        #self.driver.implicitly_wait(15)

    def openHamburgerMenu(self):
        try:
            self.driver.find_element_by_css_selector("rect[y='9']").click()
            time.sleep(1)
        except:
            print "hamburger menu click error"
            time.sleep(5)
            self.driver.find_element_by_css_selector("rect[y='9']").click()
            time.sleep(1)

        try:
            self.driver.find_element_by_css_selector("svg[class='icon icon--close icon--green ']").click()
            time.sleep(1)
        except:
            print "hamburger menu close click error"
            time.sleep(5)
            self.driver.find_element_by_css_selector("svg[class='icon icon--close icon--green ']").click()
            time.sleep(1)

        try:
            self.driver.find_element_by_css_selector("rect[y='9']").click()
            time.sleep(1)
        except:
            print "hamburger menu click error"
            time.sleep(5)
            self.driver.find_element_by_css_selector("rect[y='9']").click()
            time.sleep(1)

    def resizeBrowserWindow(self):
            x = os.environ["BROWSER_SIZE_X"]
            y = os.environ["BROWSER_SIZE_Y"]
            self.driver.set_window_size(x, y)
            print "set window size: ", x, "x",y
