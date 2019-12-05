import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class CopartComSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver_linux64/chromedriver")

    def test_challenge2(self):
        copartdriver = self.driver
        copartdriver.get("https://www.copart.com/")
        self.assertIn("Copart", copartdriver.title)
        searchelem = copartdriver.find_element_by_id("input-search")
        searchelem.send_keys("exotics")
        searchelem.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "No results found." not in copartdriver.page_source
        assert "PORSCHE" in copartdriver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
