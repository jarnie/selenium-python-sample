
from baseTest import baseTest
import unittest
import xmlrunner
import time
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class techCrunchTest(baseTest):

    def setUp(self):
        super(techCrunchTest, self).setUpFFBrowserStack()
        self.resizeBrowserWindow()

    def test_1_open_page(self):

        try:
            # test name is passed as parameter at driver teardown
            baseTest.sampleTestName = "test_1_open_page"
            self.open_page()
            baseTest.testPassed = True
        except:
            print "error"
            baseTest.testPassed = False
            self.take_screenshot(sys._getframe().f_code.co_name+"-test-failed.png")
            raise

    def test_2_open_startups(self):

        try:
            baseTest.sampleTestName = "test_2_open_startups"
            self.open_startups()
            baseTest.testPassed = True
        except:
            print "error"
            baseTest.testPassed = False
            self.take_screenshot(sys._getframe().f_code.co_name+"-test-failed.png")
            raise

    def test_3_open_apps(self):

        try:
            baseTest.sampleTestName = "test_3_open_apps"
            self.open_apps()
            baseTest.testPassed = True
        except:
            print "error"
            baseTest.testPassed = False
            self.take_screenshot(sys._getframe().f_code.co_name+"-test-failed.png")
            raise

    def test_4_search_mobile(self):

        try:
            baseTest.sampleTestName = "test_4_search_mobile"
            self.search_mobile()
            baseTest.testPassed = True
        except:
            print "error"
            baseTest.testPassed = False
            self.take_screenshot(sys._getframe().f_code.co_name+"-test-failed.png")
            raise

    def test_5_fail_test(self):

        try:
            baseTest.sampleTestName = "test_5_fail_test"
            self.fail_test()
            baseTest.testPassed = True
        except:
            print "error"
            baseTest.testPassed = False
            self.take_screenshot(sys._getframe().f_code.co_name+"-test-failed.png")
            raise

    def open_page(self):
        global testPassed,sampleTestName

        self.driver.get("https://techcrunch.com")
        self.take_screenshot()
        try:
            self.driver.find_element_by_css_selector("input[type='submit']").click()
        except NoSuchElementException:
            print "error"
        self.checkMenuElement()
        title = self.driver.title
        assert "TechCrunch" in title

    def open_startups(self):
        global testPassed,sampleTestName

        self.driver.get("https://techcrunch.com")
        self.take_screenshot()
        try:
            self.driver.find_element_by_css_selector("input[type='submit']").click()
        except NoSuchElementException:
            print "error"
        self.checkMenuElement()
        self.driver.find_element_by_css_selector("ul[class='menu navigation__main-menu'] a[href='/startups/']").click()
        time.sleep(5)
        currentUrl = self.driver.current_url
        self.take_screenshot()
        self.assertEqual(currentUrl,"https://techcrunch.com/startups/")

    def open_apps(self):
        global testPassed,sampleTestName

        self.driver.get("https://techcrunch.com")
        self.take_screenshot()
        try:
            self.driver.find_element_by_css_selector("input[type='submit']").click()
        except NoSuchElementException:
            print "error"
        self.checkMenuElement()
        self.driver.find_element_by_css_selector("ul[class='menu navigation__main-menu'] a[href='/apps/']").click()
        time.sleep(5)
        currentUrl = self.driver.current_url
        self.take_screenshot()
        self.assertEqual(currentUrl,"https://techcrunch.com/apps/")

    def search_mobile(self):
        global testPassed,sampleTestName

        self.driver.get("https://techcrunch.com")
        self.take_screenshot()
        try:
            self.driver.find_element_by_css_selector("input[type='submit']").click()
        except NoSuchElementException:
            print "error"
        self.checkMenuElement()
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

    def fail_test(self):
        global testPassed,sampleTestName

        self.driver.get("https://techcrunch.com")
        self.take_screenshot()
        try:
            self.driver.find_element_by_css_selector("input[type='submit']").click()
        except NoSuchElementException:
            print "error"
        self.checkMenuElement()
        self.driver.find_element_by_css_selector("ul[class='menu navigation__main-menu'] a[href='/apps/']").click()
        time.sleep(5)
        currentUrl = self.driver.current_url
        # scroll to the bottom of page (just for demonstration)
        self.take_screenshot("before_swipe")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.take_screenshot("after_swipe")
        # current url should not be 'fail' and test should fail here
        self.assertEqual(currentUrl,"https://techcrunch.com/fail/")

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='results'))
