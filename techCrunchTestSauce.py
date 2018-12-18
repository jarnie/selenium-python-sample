
from baseTest import baseTest
import unittest
import xmlrunner
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class techCrunchTest(baseTest):

    def setUp(self):
        super(techCrunchTest, self).setUpFFSauceLabs(baseTest.sampleTestName)

    def test_1_open_page(self):
        global testPassed,sampleTestName

        self.driver.get("https://techcrunch.com")
        self.take_screenshot()
        title = self.driver.title
        assert "TechCrunch" in title
        baseTest.testPassed = True
        baseTest.sampleTestName = "test_2_open_startups"

    def test_2_open_startups(self):
        global testPassed,sampleTestName

        self.driver.get("https://techcrunch.com")
        self.take_screenshot()
        self.driver.find_element_by_css_selector("ul[class='menu navigation__main-menu'] a[href='/startups/']").click()
        time.sleep(5)
        currentUrl = self.driver.current_url
        self.take_screenshot()
        self.assertEqual(currentUrl,"https://techcrunch.com/startups/")
        baseTest.testPassed = True
        baseTest.sampleTestName = "test_3_open_apps"

    def test_3_open_apps(self):
        global testPassed,sampleTestName

        self.driver.get("https://techcrunch.com")
        self.take_screenshot()
        self.driver.find_element_by_css_selector("ul[class='menu navigation__main-menu'] a[href='/apps/']").click()
        time.sleep(5)
        currentUrl = self.driver.current_url
        self.take_screenshot()
        self.assertEqual(currentUrl,"https://techcrunch.com/apps/")
        baseTest.testPassed = True
        baseTest.sampleTestName = "test_4_search_mobile"

    def test_4_search_mobile(self):
        global testPassed,sampleTestName

        self.driver.get("https://techcrunch.com")
        self.take_screenshot()
        self.driver.find_element_by_css_selector("label[for='nav-search-field']").click()
        time.sleep(2)
        searchField = self.driver.find_element_by_css_selector("input[class='search-form__input']")
        searchField.send_keys('mobile')
        self.take_screenshot()
        searchField.send_keys(Keys.RETURN)
        searchResult = self.driver.find_element_by_css_selector("span[class='editable-search-results']")
        searchText = searchResult.text
        self.take_screenshot()
        self.assertEqual(searchText,"mobile")
        baseTest.testPassed = True

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='results'))
