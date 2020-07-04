import unittest
import argparse
import sys
from pageobjects.GoogleSearchPage import GoogleSearchPage
from pageobjects.SearchResultsPage import SearchResultsPage
from driverInit.Browser import Browser


class RunTest(unittest.TestCase):

    def setUp(self):
        self.driver = Browser().getbrowser("chrome")
        self.driver.get("https://www.google.com/")
        self.googlesearchpage = GoogleSearchPage(self.driver)
        self.searchresultspage = SearchResultsPage(self.driver)

    def testExample(self):
        self.googlesearchpage.searchfor("mamamia pizza")
        self.searchresultspage.link_selenium_present(
            "Pizza chain Mamamia!")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    browser = argparse.ArgumentParser()
    browser.add_argument("-b", "--browser", required=False,
                         help="name of the browser", default="chrome")
    browser.add_argument('unittest_args', nargs='*')
    args = browser.parse_args()
    sys.argv[1:] = args.unittest_args
    browsername = vars(args)["browser"]
    unittest.main()
