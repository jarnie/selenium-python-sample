
from baseTest import baseTest
import unittest
import xmlrunner
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class techCrunchTest(baseTest):

    def setUp(self):
        super(techCrunchTest, self).setUpChrome()
        self.resizeBrowserWindow()

    def test_open_page(self):
        global testPassed

        self.driver.get("https://techcrunch.com")
        self.take_screenshot()
        self.driver.implicitly_wait(5)
        try:
            self.driver.find_element_by_css_selector("input[type='submit']").click()
        except NoSuchElementException:
            print "error"
        self.take_screenshot()
        self.checkMenuElement()
        self.driver.implicitly_wait(15)
        title = self.driver.title
        print title.encode('utf-8')
        assert "TechCrunch" in title
        baseTest.testPassed = True

    def test_open_startups(self):
        global testPassed

        self.driver.get("https://techcrunch.com")
        self.take_screenshot()
        self.driver.implicitly_wait(5)
        try:
            self.driver.find_element_by_css_selector("input[type='submit']").click()
        except NoSuchElementException:
            print "error"
        self.checkMenuElement()
        self.driver.implicitly_wait(15)
        title = self.driver.title
        print title.encode('utf-8')
        assert "TechCrunch" in title
        if baseTest.hamburgerMenuVisible:
            self.openHamburgerMenu()
        self.driver.find_element_by_css_selector("ul[class='menu navigation__main-menu'] a[href='/startups/']").click()
        time.sleep(5)
        currentUrl = self.driver.current_url
        self.take_screenshot()
        #assert "https://techcrunch.com/startups/" currentUrl
        self.assertEqual(currentUrl,"https://techcrunch.com/startups/")
        baseTest.testPassed = True

    def test_open_apps(self):
        global testPassed

        self.driver.get("https://techcrunch.com")
        self.take_screenshot()
        self.driver.implicitly_wait(5)
        try:
            self.driver.find_element_by_css_selector("input[type='submit']").click()
        except NoSuchElementException:
            print "error"
        self.checkMenuElement()
        self.driver.implicitly_wait(15)
        title = self.driver.title
        print title.encode('utf-8')
        assert "TechCrunch" in title
        if baseTest.hamburgerMenuVisible:
            self.openHamburgerMenu()
        self.driver.find_element_by_css_selector("ul[class='menu navigation__main-menu'] a[href='/apps/']").click()
        time.sleep(5)
        currentUrl = self.driver.current_url
        self.take_screenshot()
        self.assertEqual(currentUrl,"https://techcrunch.com/apps/")
        baseTest.testPassed = True

    def test_search_mobile(self):
        global testPassed

        self.driver.get("https://techcrunch.com")
        self.take_screenshot()
        self.driver.implicitly_wait(5)
        try:
            self.driver.find_element_by_css_selector("input[type='submit']").click()
        except NoSuchElementException:
            print "error"
        self.checkMenuElement()
        self.driver.implicitly_wait(15)
        title = self.driver.title
        print title.encode('utf-8')
        assert "TechCrunch" in title
        if baseTest.hamburgerMenuVisible:
            self.openHamburgerMenu()
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
