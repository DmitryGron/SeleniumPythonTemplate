from selenium.webdriver.common.by import By
import re


class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver

    def link_selenium_present(self, text):
        src = self.driver.page_source
        assert (text in self.driver.page_source)
        assert self.driver.find_element_by_partial_link_text(
            text).is_displayed()
        self.driver.find_element_by_partial_link_text(
            text).click()
