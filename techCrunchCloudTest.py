
from baseTest import baseTest
import unittest
import xmlrunner
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class techCrunchCloudTest(baseTest):

    def setUp(self):
        super(techCrunchCloudTest, self).setUpChromeBitbar()

    def test_open_page(self):
        self.driver.get("https://techcrunch.com")
        self.take_screenshot()
        self.driver.implicitly_wait(5)
        try:
            self.driver.find_element_by_css_selector("input[type='submit']").click()
        except: # catch *all* exceptions
            print "error"
        self.take_screenshot()
        self.driver.implicitly_wait(15)
        title = self.driver.title
        assert "TechCrunch" in title

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='results'))
