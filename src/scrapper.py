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
        self._driver = None
        self._page_source = None
        self._text = None

    def _create_driver(self):
        """
        Create Selenium Web _driver
        """
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")
        self._driver = webdriver.Chrome(options=options)
        if self._driver:
            return True
        return False

    def _input_url(self):
        """
        Input url
        """
        val = input("Enter a url: ")
        if validators.url(val):
            wait = WebDriverWait(self._driver, 10)
            self._driver.get(val)
            wait.until(EC.url_to_be(val))
            if self._driver.current_url == val:
                self._page_source = self._driver.page_source
                return True
        return False

    def set_url(self, val):
        """
        set url
        """
        if validators.url(val):
            wait = WebDriverWait(self._driver, 10)
            self._driver.get(val)
            wait.until(EC.url_to_be(val))
            if self._driver.current_url == val:
                self._page_source = self._driver.page_source
                return True
        return False

    def _scroll_and_get_text(self):
        """
        Get url text
        """
        page_height = self._driver.execute_script("return document.documentElement.scrollHeight")
        while True:
            self._driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            new_height = self._driver.execute_script("return document.documentElement.scrollHeight")
            if new_height == page_height:
                break
            page_height = new_height
        status = False
        soup = BeautifulSoup(self._page_source, "html.parser")
        for element in soup(["script", "style"]):  # убираем скрипты и стиль
            element.extract()
        strips = list(soup.stripped_strings)  # собираем весь текст в список
        text = '\n'.join(strips)
        self._text = text.encode("utf-8")  # избавляемся от возможных ошибок
        if len(self._text) > 0:
            status = True
        return status

    def _save_text_to_file(self, filename):
        """
        Save text to file
        """
        with(open(filename, 'wb')) as output_file:
            output_file.write(self._text)
            output_file.close()

    def validate_driver(self):
        """validates driver"""
        if self._create_driver():
            pass
        else:
            print('Cannot create scrapper')

    def validate_input(self):
        """validates input"""
        if self._input_url():
            pass
        else:
            print('Error while input URL')

    def validate_text(self):
        """validates url text"""
        if self._scroll_and_get_text():
            self._save_text_to_file('URL-text.txt')
        else:
            print('Error while getting url text')
