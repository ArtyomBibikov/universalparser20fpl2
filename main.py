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

    def createDriver(self):
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

    def getText(self):
        """
        Get url text
        """
        status = False
        soup = BeautifulSoup(self.page_source, "html.parser")
        for element in soup(["script", "style"]):  # убираем скрипты и стиль
            element.extract()
        strips = list(soup.stripped_strings)  # собираем весь текст в список
        text = '\n'.join(strips)
        self.text = text.encode("utf-8")  # избавляемся от возможных ошибок
        if len(self.text) > 0:
            status = True
        return status

    def saveTextToFile(self, filename):
        """
        Save text to file
        """
        fl = open(filename, 'wb')
        fl.write(self.text)
        fl.close()

if __name__ == "__main__":
    scrapper = Scrapper()
    if scrapper.createDriver():
        if scrapper.input_url():
            if scrapper.getText():
                scrapper.saveTextToFile('URL-text.txt')
            else:
                print('Error while getting url text')
        else:
            print('Error while input URL')
    else:
        print('Cannot create scrapper')
