from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome()

val = input("Enter a url: ")
wait = WebDriverWait(driver, 10)
driver.get(val)
wait.until(EC.url_to_be(val))
if driver.current_url == val:
    page_source = driver.page_source

soup = BeautifulSoup(page_source, "html.parser")
for element in soup(["script", "style"]): #убираем скрипты и стиль
    element.extract()
strips = list(soup.stripped_strings) #собираем весь текст в список
text = '\n'.join(strips)
text = text.encode("utf-8") #избавляемся от возможных ошибок
savetofile = open('outfile.txt', 'wb')
savetofile.write(text)
