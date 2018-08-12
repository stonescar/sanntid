from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time


class Stop():
    def __init__(self, stop_id, line, destination=""):
        self.stop_id = stop_id
        self.line = line
        self.dest = destination

        self.browser = self.setup_driver()

    def setup_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")

        chrome_driver = os.getcwd() + "\\..\\assets\\chromedriver.exe"

        return webdriver.Chrome(chrome_options=chrome_options,
                                executable_path=chrome_driver)

    def get_next_departure(self):
        url = "http://bartebuss.no/%s" % self.stop_id

        self.browser.get(url)

        time.sleep(1)

        table = BeautifulSoup(
            self.browser.find_element_by_css_selector("#realtimeSchedule")
            .get_attribute("innerHTML"), "html.parser")

        for row in table.find_all("tr"):
            correct_line = row.find(class_="line").string == self.line
            correct_dest = row.find(class_="destination") == self.dest

            if correct_line and (correct_dest or self.dest == ""):
                return row.find(class_="timeFormatted").string
