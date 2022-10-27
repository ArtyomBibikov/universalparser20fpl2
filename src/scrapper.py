"""The selenium library contains various tools for scanning and parsing webpages
BeautifulSoup parses the raw text data and only takes what is relevant for our study"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import validators


class Scrapper:
    """
    Web page scrapper
    """

    def __init__(self):
        """Constructor"""
        self.driver = None
        self.page_source = None
        self.text = None

    def create_driver(self):
        """
        Create Selenium Web Driver
        """
        status = False
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")
        self.driver = webdriver.Chrome(options=options)
        if self.driver:
            status = True
        return status

    def input_url(self):
        """
        Input url
        """
        status = False
        val = input("Enter a url: ")
        if validators.url(val):
            wait = WebDriverWait(self.driver, 10)
            self.driver.get(val)
            wait.until(EC.url_to_be(val))
            if self.driver.current_url == val:
                self.page_source = self.driver.page_source
                status = True
        return status

    def set_url(self, val):
        """
        set url
        """
        status = False
        if validators.url(val):
            wait = WebDriverWait(self.driver, 10)
            self.driver.get(val)
            wait.until(EC.url_to_be(val))
            if self.driver.current_url == val:
                self.page_source = self.driver.page_source
                status = True

        return status

    def scroll_and_get_text(self):
        """
        Get url text
        """
        page_height = self.driver.execute_script("return document.documentElement.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            new_height = self.driver.execute_script("return document.documentElement.scrollHeight")
            if new_height == page_height:
                break
            page_height = new_height
        status = False
        soup = BeautifulSoup(self.page_source, "html.parser")
        for element in soup(["script", "style"]):  # убираем скрипты и стиль
            element.extract()
        strips = list(soup.stripped_strings)  # собираем весь текст в список
        text = '\n'.join(strips)
        self.text = text.encode("utf-8")  # избавляемся от возможных ошибок
        if len(self.text) > 0:
            status = True
        return text
